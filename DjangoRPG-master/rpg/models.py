from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=32)
    bio = models.CharField(max_length=500)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hp = models.FloatField()
    mana = models.FloatField()
    energy = models.FloatField()
    lvl = models.IntegerField()
