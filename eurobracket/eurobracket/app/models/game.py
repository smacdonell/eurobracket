from django.db import models

from eurobracket.app.models import Team


class Round(models.Model):
    name = models.CharField(max_length=64)
    ref_code = models.CharField(max_length=64)
    points = models.IntegerField()

    class Meta:
        db_table = 'round'


class Game(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one')
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two')
    team_one_score = models.IntegerField()
    team_two_score = models.IntegerField()
    game_happened = models.BooleanField(default=False)

    class Meta:
        db_table = 'game'
