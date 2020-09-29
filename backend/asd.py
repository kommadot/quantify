import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "backend.settings") 
import django 
django.setup()

from api.models import StockPrice

SP = StockPrice.objects.all()
print(SP[1:100][0])