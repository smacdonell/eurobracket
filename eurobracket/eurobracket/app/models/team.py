from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'team'


class TeamStatus(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'team_status'

