from django.utils import timezone
from django.db import models
from datetime import datetime

class Simulation(models.Model):
    id = models.IntegerField(primary_key=True)
    # user_id = models.ForeignKey('user.id',on_delete=models.CASCADE)
    user_id = models.IntegerField()
    item_code = models.CharField(max_length=6)
    item_name = models.CharField(max_length=20)
    price = models.IntegerField()
    buy_date = models.DateTimeField(default=datetime.now)
    quantity = models.IntegerField()
    

class SimulationBreakdown(models.Model):
    id = models.IntegerField(primary_key=True)
    # user_id = models.ForeignKey('user.id',on_delete=models.CASCADE)
    user_id = models.IntegerField()
    item_code = models.CharField(max_length=6)
    item_name = models.CharField(max_length=20)
    price = models.IntegerField()
    buy_date = models.DateTimeField()
    quantity = models.IntegerField()
    sell_price = models.IntegerField()
    sell_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return f"{self.item_code} , {self.price} , {self.buy_date} , {self.sell_date}"