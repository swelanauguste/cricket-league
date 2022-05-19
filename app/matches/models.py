from django.db import models
from players.models import Player
from teams.models import Team
from tournaments.models import Tournament


class HowOut(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Venue(models.Model):
    venue_name = models.CharField(max_length=50)
    venue_name_short = models.CharField(max_length=10)

    def __str__(self):
        return self.venue_name


class Match(models.Model):
    date = models.DateField()
    match_venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, null=True, blank=True
    )
    team1 = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team1", null=True, blank=True
    )
    team2 = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team2", null=True, blank=True
    )
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "Matches"
   
    @property   
    def get_scores(self):
        # all_batter_scores = 
        return sum([batter.runs for batter in self.batters.all()])

    def __str__(self):
        return f"{self.team1.team_name} vs {self.team2.team_name} {self.get_scores}"


class MatchBatter(models.Model):
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE, null=True, blank=True, related_name="batters"
    )
    batter = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    runs = models.IntegerField(default=0)
    balls_faced = models.IntegerField("b/f", default=0)
    how_out = models.ForeignKey(HowOut, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.batter.player_name} {self.runs}/{self.balls_faced}"
