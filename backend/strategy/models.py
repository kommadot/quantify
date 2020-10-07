from django.db import models

# Create your models here.
class LowVariability(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    variability = models.FloatField()


class Momentum(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    momentum = models.FloatField()


class RiskMomentum(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    risk_momentum = models.FloatField()


class Value(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    per = models.FloatField()
    pbr = models.FloatField()
    psr = models.FloatField()
    rank = models.CharField(max_length=100)


class Quality(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    sum = models.IntegerField()