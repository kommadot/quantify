from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()
    category = models.CharField(max_length=400)
    main = models.CharField(max_length=400)