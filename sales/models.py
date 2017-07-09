from django.db import models

from games.models import Game
from users.models import Profile

class Sale(models.Model):
    game_id = models.ForeignKey(Game,on_delete = models.CASCADE)
    user = models.ForeignKey(Profile)
    amount = models.FloatField(default = 0)
    created_at = models.DateTimeField()
    def __str__(self):
        return self.id