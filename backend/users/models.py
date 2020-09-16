from djongo import models


class User(models.Model):
    nickname = models.CharField(max_length=20)
    social_id = models.CharField(max_length=30)
    platform = models.CharField(max_length=10)
    budget = models.FloatField(default=10000000)