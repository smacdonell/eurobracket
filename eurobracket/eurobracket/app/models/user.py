from django.contrib.auth.models import User
from django.db import models


class UserState(models.Model):
    state = models.CharField(max_length=64)

    class Meta:
        db_table = 'user_state'


class UserStateRel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.ForeignKey(UserState, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_state_rel'
