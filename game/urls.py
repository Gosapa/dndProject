from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('create/<int:gameID>/', views.create_Character, name='create_character'),
    path('createGame/', views.create_Game, name="create_game"),
    path('chat/<int:gameID>', views.chat, name="chat"),
    path('list/', views.list, name="list"),
    path('detail/<int:gameID>', views.detail, name="detail"),
]
