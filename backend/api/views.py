from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from . import price
import json
from .serialization import StockPriceSerializer,StockSerializer,CompanySerializer
from .models import StockPrice,Stock,Company
# Create your views here.
@permission_classes((AllowAny,))
class Price(APIView):
    def get(self,request,code):
        stock_price = price.get_price(code)
        price_json = {'code':code,'price':int(stock_price.replace(",",""))}
        return Response(price_json,status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class BeforePrice(APIView):
    def get(self,request,code):
        stock_price = price.get_before_price(code)
        price_json = {'code':code,'price':int(stock_price.replace(",",""))}
        return Response(price_json,status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class StockPriceDetail(APIView):
    def get(self,request,code):
        sp = StockPrice.objects.get(code=code)
        return Response(StockPriceSerializer(sp).data,status=status.HTTP_200_OK)
        

@permission_classes((AllowAny,))
class CompanyAll(APIView):
    def get(self,request):
        comp = Company.objects.all()
        return Response(CompanySerializer(comp,many=True).data,status=status.HTTP_200_OK)
        