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
from django.db.models import Q
from django.forms.models import model_to_dict
from bson.objectid import ObjectId
from users.serializers import UserSerializer
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class SimulationList(APIView):
    queryset = Simulation.objects.all()
    serializer_class = SimulationSerializer
    

    def get(self, request):
        user = request.user
        simulations = Simulation.objects.filter(user_id = user.user_id)
        # simulations = Simulation.objects.all()
        print(user.user_id)
        # return Response(UserSerializer(user).data,status=status.HTTP_200_OK)
        return Response(self.serializer_class(simulations,many=True).data,status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        user = request.user
        code = request.data['code']
        name = request.data['name']
        
        quantity = int(request.data['quantity'])
        price = int(request.data['price'])
        temp_simulation = Simulation.objects.filter(Q(user_id = user.user_id) & Q(item_code = code)).first()
        temp_budget = user.budget - price*quantity
        if temp_budget <0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user.budget = user.budget-price*quantity
        user.save()
        if not temp_simulation:
            simulation = Simulation(user_id = user.user_id, item_code = code, item_name = name, price = price, quantity = quantity)
            simulation.save()

        else:
            # temp_simulation = temp_simulation[0]
            pk = temp_simulation._id
            simulation = Simulation.objects.get(pk = pk)
            simulation.price = (temp_simulation.price * temp_simulation.quantity + price * quantity)/(temp_simulation.quantity + quantity)
            simulation.quantity = temp_simulation.quantity + quantity
            simulation.save()

        return Response(status = status.HTTP_201_CREATED)

@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class SimulationDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  generics.GenericAPIView):
    
    queryset = Simulation.objects.all()
    serializer_class = SimulationSerializer

    
    def get(self, request, oid):

        simulation = Simulation.objects.get(_id = ObjectId(oid))
        return Response(self.serializer_class(simulation).data,status=status.HTTP_200_OK)


    @transaction.atomic
    def delete(self,request,oid,format=None):
        user =  request.user
        
        simulation = Simulation.objects.get(_id = ObjectId(oid))
        sell_price = request.data['sell_price']

        user.budget += sell_price * simuation.quantity
        user.save()
        
        simulationbreakdown = SimulationBreakdown(user_id=simuation.user_id,item_code=simuation.item_code,item_name=simuation.item_name,price=simuation.price,
                                                  buy_date=simuation.buy_date,quantity=simuation.quantity,sell_price=sell_price)
        simulationbreakdown.save()
        simuation.delete()
        return Response(status=status.HTTP_200_OK)

@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class SimulationBreakdownList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = SimulationBreakdown.objects.all()
    serializer_class = SimulationBreakdownSerializer
    
    def get(self, request, *args, **kwargs):
        user = request.user
        simulations = SimulationBreakdown.objects.filter(user_id = user.user_id)
        return Response(serializer_class(simulations).data,status=status.HTTP_200_OK)

@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
class SimulationBreakdownDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  generics.GenericAPIView):
    queryset = SimulationBreakdown.objects.all()
    serializer_class = SimulationBreakdownSerializer
    
    def get(self, request,oid):
        user = request.user
        simulationBreakdown = SimulationBreakdown.objects.get(_id = ObjectId(oid))
        return Response(serializer_class(simulationBreakdown).data,status=status.HTTP_200_OK)
