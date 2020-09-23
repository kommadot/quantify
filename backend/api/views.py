from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from . import price
import json
# Create your views here.
@permission_classes((AllowAny,))
class StockPrice(APIView):
    def get(self,request,code):
        stock_price = price.get_price(code)
        price_json = {'code':code,'price':int(stock_price.replace(",",""))}
        return Response(price_json,status=status.HTTP_200_OK)