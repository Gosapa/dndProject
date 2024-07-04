from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import CharacterForm
from .models import *
import gemini.functions as geminiResponse

# Create your views here.

@login_required
def create_Character(request, gameID):
    game = Game.objects.get(id=gameID)
    user_character_cnt = Character.objects.filter(game=game, is_user=True).count()
    if user_character_cnt >= 1:
        return redirect('game:chat', gameID=gameID)
    form = CharacterForm(request.POST or None)
    if form.is_valid():
        character = form.save(commit=False)
        response = geminiResponse.create_stat(name=character.name, origin=character.origin, gender=character.gender, plot=character.plot)
        character.game= game
        character.is_user = True
        character.stat = response['stats']
        character.save()
        game.name = f"{character.name}'s game"
        game.save()
        return redirect('game:chat', gameID=gameID)
    return render(request, 'game/createCharacter.html', {'form': form})


@login_required
def create_Game(request):
    if request.method == "POST":
        if Game.objects.filter(user=request.user).count() >= 3:
            return JsonResponse({"message": "User already has 3 games."}, status=202)
        game = Game.objects.create(
            name = "Default_Game_Name",
            setting = "Default_Setting",
            user = request.user
        )
        return JsonResponse({"message": "Game Successfully Created.", "gameID": game.id}, status=200)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=400)
    
@login_required
def chat(request, gameID):
    game = Game.objects.get(id=gameID)
    return render(request, 'game/gamechat.html', {'game': game})

@login_required
def list(request):
    currentUser = request.user
    saved_games = Game.objects.filter(user=currentUser)
    return render(request, 'game/list.html', {'games': saved_games})

@login_required
def detail(request, gameID):
    game = Game.objects.get(id=gameID)
    try:
        user_character = Character.objects.get(game=game, is_user=True)
        return render(request, 'game/gameDetail.html', {'game':game, 'user_character': user_character})
    except Character.DoesNotExist:
        return redirect('game:create_character', gameID=gameID)