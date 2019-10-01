from django.db import models


class Classement(models.Model):
    equipe = models.CharField(max_length=40, unique=True)
    jouer = models.IntegerField(default=0)
    gagner = models.IntegerField(default=0)
    nul = models.IntegerField(default=0)
    perdu = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.equipe


class Calendrier(models.Model):
    journee = models.IntegerField()
    equipeA = models.CharField(max_length=50)
    equipeB = models.CharField(max_length=50)
    goalA = models.IntegerField(blank=True, default=0)
    goalB = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.equipeA+" "+self.equipeB
