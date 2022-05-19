from django.db import models


class District(models.Model):
    district_name = models.CharField(max_length=100)
    district_name_abbreviation = models.CharField(max_length=4)

    def __str__(self):
        return self.district_name
