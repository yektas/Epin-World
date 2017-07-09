from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=225)
    game_pin_price = models.FloatField(default=0)
    created_at = models.DateField()
    popularity = models.IntegerField(default=1)
    game_logo = models.CharField(max_length=250)

    def __str__(self):
        return self.name
