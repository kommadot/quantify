from rest_framework import serializers
from .models import SimulationBreakdown,Simulation

class SimulationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Simulation
        fields = '__all__'

        
class SimulationBreakdownSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SimulationBreakdown
        fields = '__all__'
