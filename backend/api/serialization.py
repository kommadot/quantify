from rest_framework import serializers
from .models import StockPrice,Stock,Company

class StockPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockPrice
        fields = '__all__'

        
class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stock
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'