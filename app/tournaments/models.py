from django.db import models


class Year(models.Model):
    year = models.IntegerField(default=0)

    def __str__(self):
        return str(self.year)


class Version(models.Model):
    version = models.CharField(max_length=100)

    def __str__(self):
        return self.version


class Tournament(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, blank=True, null=True)
    version = models.ForeignKey(
        Version, on_delete=models.CASCADE, blank=True, null=True
    )
    tournament_name = models.CharField(max_length=100, unique=True)
    tournament_date = models.DateField()

    def __str__(self):
        return self.tournament_name
