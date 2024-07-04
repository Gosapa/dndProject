from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('<int:gameID>/create/', views.create_Character, name='create_character'),
    path('createGame/', views.create_Game, name="create_game"),
    path('chat/<int:gameID>', views.chat, name="chat"),
]
