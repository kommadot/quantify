from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from . import price
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Company

# Create your views here.
@permission_classes((AllowAny,))
class StockPrice(APIView):
    def get(self,request,code):
        stock_price = price.get_price(code)
        price_json = {'code':code,'price':int(stock_price.replace(",",""))}
        return Response(price_json,status=status.HTTP_200_OK)


@csrf_exempt
def findCompany(request):
    word = '%s' %request.POST['word']
    post = Company.objects.filter(
        Q(code__icontains=word) | Q(name__icontains=word)
    ).distinct()
    return JsonResponse(post, safe=False)


@csrf_exempt
def Companylist(request):
    if request.method == 'GET':
        post = list(Company.objects.values())
        return JsonResponse(post, safe=False)