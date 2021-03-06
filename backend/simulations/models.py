from django.utils import timezone
from djongo import models
from datetime import datetime

class Simulation(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    # user_id = models.ForeignKey('user.id',on_delete=models.CASCADE)
    user_id = models.CharField(max_length=64)
    item_code = models.CharField(max_length=6)
    item_name = models.CharField(max_length=20)
    price = models.IntegerField()
    buy_date = models.DateTimeField(default=datetime.now)
    quantity = models.IntegerField()
    

class SimulationBreakdown(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    # user_id = models.ForeignKey('user.id',on_delete=models.CASCADE)
    user_id = models.CharField(max_length=64)
    item_code = models.CharField(max_length=6)
    item_name = models.CharField(max_length=20)
    price = models.IntegerField()
    buy_date = models.DateTimeField()
    quantity = models.IntegerField()
    sell_price = models.IntegerField()
    sell_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return f"{self.item_code} , {self.price} , {self.buy_date} , {self.sell_date}"