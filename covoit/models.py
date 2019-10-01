from django.db import models
from connexion.models import User


class Voiture(models.Model):

    conduct = models.ForeignKey(User, on_delete=models.CASCADE)
    placedispo = models.IntegerField(default=0)
    placelibre = models.IntegerField(default=0)
    heure = models.IntegerField(default=0)
    minute = models.IntegerField(default=0)
    départ = models.CharField(max_length=255)
    p1 = models.IntegerField(null=True, blank=True)
    addr1 = models.CharField(max_length=255, null=True, blank=True)
    p2 = models.IntegerField(null=True, blank=True)
    addr2 = models.CharField(max_length=255, null=True, blank=True)
    p3 = models.IntegerField(null=True, blank=True)
    addr3 = models.CharField(max_length=255, null=True, blank=True)
    p4 = models.IntegerField(null=True, blank=True)
    addr4 = models.CharField(max_length=255, null=True, blank=True)
    p5 = models.IntegerField(null=True, blank=True)
    addr5 = models.CharField(max_length=255, null=True, blank=True)
    p6 = models.IntegerField(null=True, blank=True)
    addr6 = models.CharField(max_length=255, null=True, blank=True)
    p7 = models.IntegerField(null=True, blank=True)
    addr7 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.conduct
