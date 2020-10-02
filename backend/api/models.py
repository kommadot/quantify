# from django.db import models
from djongo import models
import djongo
# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=6)

class StockRow(models.Model):
    time = models.CharField(max_length=100)
    open = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    close = models.IntegerField()
    volume = models.IntegerField()

    class Meta:
        abstract = True

class StockPrice(models.Model):
    code = models.CharField(max_length=6)
    data = models.ArrayField(model_container=StockRow)
    name = models.CharField(max_length=100)
    market_price = models.IntegerField()

class Company(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    category = models.CharField(max_length=400)
    main = models.CharField(max_length=400)