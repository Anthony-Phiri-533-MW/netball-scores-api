from django.db import models
from django.utils import timezone

class Scores(models.Model):
    team1name = models.CharField(max_length=200) 
    team1scores = models.IntegerField(max_length=240)
    team2name = models.CharField(max_length=200) 
    team2scores =models.IntegerField(max_length=240)
    league = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.team1name + " vs " + self.team2name + " " + str(self.date)