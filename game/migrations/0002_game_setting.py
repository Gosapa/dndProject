# Generated by Django 5.0.6 on 2024-07-02 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='setting',
            field=models.CharField(default='null', max_length=100),
        ),
    ]