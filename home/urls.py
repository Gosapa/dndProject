from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.home, name="signin"),
    path('start/', views.start, name="start"),
    path('', views.redir, name="redirect"),
]
