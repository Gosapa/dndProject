# Generated by Django 5.0.6 on 2024-07-02 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_game_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='name',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
