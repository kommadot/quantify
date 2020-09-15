from rest_framework import serializers
from .models import LowVariability
from .models import Momentum
from .models import RiskMomentum


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