from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def redir(request):
    return redirect('start')

def home(request):
    return render(request, 'home/home.html')

@login_required
def start(request):
    return render(request, 'home/start.html')

