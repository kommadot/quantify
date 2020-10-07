from .models import LowVariability, Momentum, RiskMomentum, Value, Quality
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import json
from .serializers import MomentumSerializer, LowVariabilitySerializer, RiskMomentumSerializer, ValueSerializer, QualitySerializer
from django.core.cache import cache

@permission_classes((AllowAny,))
class MomentumView(APIView):
    def get(self,request):
        momentum = cache.get_or_set("momentum",Momentum.objects.all())
        return Response(MomentumSerializer(momentum,many=True).data,status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class QualityView(APIView):
    def get(self,request):
        quality = cache.get_or_set("quality",Quality.objects.all())
        return Response(QualitySerializer(quality,many=True).data,status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class RiskMomentumView(APIView):
    def get(self,request):
        riskMomentum = cache.get_or_set("risk_momentum",RiskMomentum.objects.all())
        return Response(RiskMomentumSerializer(riskMomentum,many=True).data,status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class ValueView(APIView):
    def get(self,request):
        value = cache.get_or_set("value",Value.objects.all())
        return Response(ValueSerializer(value,many=True).data,status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class LowVariabilityView(APIView):
    def get(self,request):
        lowVariability = cache.get_or_set("low_variability",LowVariability.objects.all())
        return Response(LowVariabilitySerializer(lowVariability,many=True).data,status=status.HTTP_200_OK)