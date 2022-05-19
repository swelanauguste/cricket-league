from district.models import District
from django.db import models
from teams.models import Team


class BattingStyle(models.Model):
    bat_style = models.CharField(max_length=100)

    def __str__(self):
        return self.bat_style


class BowlingStyle(models.Model):
    bowl_style = models.CharField(max_length=100)

    def __str__(self):
        return self.bowl_style


class Player(models.Model):
    player_name = models.CharField(max_length=100, unique=True)
    player_dob = models.DateField()
    bat_style = models.ForeignKey(
        BattingStyle, on_delete=models.CASCADE, blank=True, null=True
    )
    bowl_style = models.ForeignKey(
        BowlingStyle, on_delete=models.CASCADE, blank=True, null=True
    )
    teams = models.ManyToManyField(Team, blank=True)

    def __str__(self):
        return self.player_name
