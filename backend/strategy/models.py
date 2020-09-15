from django.db import models

# Create your models here.
class LowVariability(models.Model):
    name = models.CharField(max_length=200)
    variability = models.FloatField()


class Momentum(models.Model):
    name = models.CharField(max_length=200)
    momentum = models.FloatField()


class RiskMomentum(models.Model):
    name = models.CharField(max_length=200)
    risk_momentum = models.FloatField()