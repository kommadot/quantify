from rest_framework import serializers
from .models import BacktestModel

class BacktestModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = BacktestModel
        fields = '__all__'

        
