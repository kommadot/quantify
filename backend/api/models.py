# from django.db import models
from djongo import models
import djongo
# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=6)

class StockPrice(models.Model):
    code = models.CharField(max_length=6)
    data = models.JSONField()

class Company(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    category = models.CharField(max_length=400)
    main = models.CharField(max_length=400)