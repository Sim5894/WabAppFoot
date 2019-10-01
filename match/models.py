from django.db import models


class MatchsRonvau(models.Model):
    equipeA = models.CharField(max_length=50)
    equipeB = models.CharField(max_length=50)
    journee = models.IntegerField()

    def __str__(self):
        return self.journee


class JoueursSelect(models.Model):
    journee = models.IntegerField(unique=True)
    j1 = models.IntegerField(blank=True, null=True)
    j2 = models.IntegerField(blank=True, null=True)
    j3 = models.IntegerField(blank=True, null=True)
    j4 = models.IntegerField(blank=True, null=True)
    j5 = models.IntegerField(blank=True, null=True)
    j6 = models.IntegerField(blank=True, null=True)
    j7 = models.IntegerField(blank=True, null=True)
    j8 = models.IntegerField(blank=True, null=True)
    j9 = models.IntegerField(blank=True, null=True)
    j10 = models.IntegerField(blank=True, null=True)
    j11 = models.IntegerField(blank=True, null=True)
    j12 = models.IntegerField(blank=True, null=True)
    j13 = models.IntegerField(blank=True, null=True)
    j14 = models.IntegerField(blank=True, null=True)
    j15 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.journee

