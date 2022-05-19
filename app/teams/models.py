from district.models import District
from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    team_name_abbreviation = models.CharField(max_length=4)

    def __str__(self):
        return self.team_name
