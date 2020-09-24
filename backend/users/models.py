from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_id = models.CharField(max_length=64,primary_key=True)
    social_id = models.CharField(max_length=30)
    platform = models.CharField(max_length=10)
    budget = models.FloatField(default=10000000)
    def __str__(self):
        return f"{self.social_id} , {self.platform} , {self.id}"