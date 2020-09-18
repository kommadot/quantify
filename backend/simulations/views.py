from django.shortcuts import render
from simulations.models import Simulation,SimulationBreakdown
from simulations.serializers import SimulationSerializer,SimulationBreakdownSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.db import transaction
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from users.models import User

class SimulationList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Simulation.objects.all()
    serializer_class = SimulationSerializer
    
    @permission_classes((IsAuthenticated,))
    @authentication_classes((JSONWebTokenAuthentication,))
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self, request, *args, **kwargs):
        #돈 다운
        return self.create(request,*args,**kwargs)
    
class SimulationDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  generics.GenericAPIView):
    
    queryset = Simulation.objects.all()
    serializer_class = SimulationSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @transaction.atomic
    def delete(self,request,pk,format=None):
        simuation = Simulation.objects.get(pk=pk)
        sell_price = request.data['sell_price']
        #user돈 업
        simulationbreakdown = SimulationBreakdown(user_id=simuation.user_id,item_code=simuation.item_code,item_name=simuation.item_name,price=simuation.price,
                                                  buy_date=simuation.buy_date,quantity=simuation.quantity,sell_price=sell_price)
        simulationbreakdown.save()
        simuation.delete()
        return Response(SimulationBreakdownSerializer(simulationbreakdown).data,status=status.HTTP_200_OK)

class SimulationBreakdownList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = SimulationBreakdown.objects.all()
    serializer_class = SimulationBreakdownSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

class SimulationBreakdownDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  generics.GenericAPIView):
    queryset = SimulationBreakdown.objects.all()
    serializer_class = SimulationBreakdownSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
