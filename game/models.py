from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50, default="")
    setting = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Character(models.Model):
    ORIGIN_CHOICES = {
        'origin1': 'origin1',
        'origin2': 'origin2',
        'origin3': 'origin3',
        'origin4': 'origin4',
    }

    GENDER_CHOICES = {
        'male': 'male',
        'female': 'female',
        'other': 'other',
    }

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="defaultname")
    origin = models.CharField(max_length=7, choices=ORIGIN_CHOICES, default='origin1')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    is_user = models.BooleanField(default=False)
    plot = models.CharField(max_length=500, default="defaultplot")
    stat = models.JSONField(default=dict)
    

    def __str__(self):
        return f'{self.game.name}\'s character {self.name}'

class Log(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)