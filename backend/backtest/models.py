from django.utils import timezone
from djongo import models
from datetime import datetime
from django.conf import settings

class Stock(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()
    class Meta:
        abstract = True

class Log(models.Model):
    date = models.CharField(max_length=100)
    datas = models.ArrayField(model_container = Stock)
    types = models.CharField(max_length=4)
    class Meta:
        abstract = True

class BacktestDate(models.Model):
    date = models.CharField(max_length=100)
    budget = models.IntegerField()
    
    class Meta:
        abstract = True
# Create your models here.
class BacktestModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = models.ArrayField(model_container=BacktestDate)
    strategy = models.IntegerField(default=1)
    log = models.ArrayField(model_container=Log)
    rebalance = models.IntegerField(default=1)

