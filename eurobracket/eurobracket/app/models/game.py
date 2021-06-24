from django.db import models

from eurobracket.app.models import Team, User


class Round(models.Model):
    name = models.CharField(max_length=64)
    ref_code = models.CharField(max_length=64)
    points = models.IntegerField()

    class Meta:
        db_table = 'round'


class Game(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one', blank=True, null=True)
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two', blank=True, null=True)
    team_one_score = models.IntegerField()
    team_two_score = models.IntegerField()
    game_happened = models.BooleanField(default=False)

    class Meta:
        db_table = 'game'


class GameRel(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    prev_game_one = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='prev_game_one', blank=True, null=True)
    prev_game_two = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='prev_game_two', blank=True, null=True)
    next_game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='next_game', blank=True, null=True)

    class Meta:
        db_table = 'game_rel'


class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    winning_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winning_team')
    losing_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='losing_team')
    round = models.ForeignKey(Round, on_delete=models.CASCADE)

    class Meta:
        db_table = 'prediction'
