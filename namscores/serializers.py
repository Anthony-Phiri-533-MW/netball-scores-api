from rest_framework import serializers
from .models import Scores

class ScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scores
        fields = ['id', 'team1name', 'team1scores', 'team2name', 'team2scores', 'league', 'date']

