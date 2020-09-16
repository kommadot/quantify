from rest_framework import serializers
from .models import LowVariability, Momentum, RiskMomentum, Value, Quality



class LowVariabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LowVariability
        fields = '__all__'

class MomentumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Momentum
        fields = '__all__'

class RiskMomentumSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskMomentum
        fields = '__all__'

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'

class QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quality
        fields = '__all__'