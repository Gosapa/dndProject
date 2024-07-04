from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import CharacterForm
from .models import *
import gemini.functions as geminiResponse

# Create your views here.

@login_required
def create_Character(request, gameID):
    form = CharacterForm(request.POST or None)
    if form.is_valid():
        game = Game.objects.get(id=gameID)
        character = form.save(commit=False)
        response = geminiResponse.create_stat(name=character.name, origin=character.origin, gender=character.gender, plot=character.plot)
        character.game= game
        character.is_user = True
        character.stat = response['stats']
        character.save()
        return redirect('game:chat', gameID=gameID)
    return render(request, 'game/createCharacter.html', {'form': form})


@login_required
def create_Game(request):
    if request.method == "POST":
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
