from django.db import models
from django.contrib.auth.models import User

from games.models import Game

class Profile(models.Model):
    user = models.OneToOneField(User)
    game = models.ForeignKey(Game)
    birth_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default = True)
    balance = models.FloatField(default = 0)
    def __str__(self):
        return self.user.username
