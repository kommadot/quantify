from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import LowVariability, Momentum, RiskMomentum, Value, Quality

# Create your views here.
@csrf_exempt
def lowvarlist(request):
    if request.method == 'GET':
        post = list(LowVariability.objects.values())
        return JsonResponse(post, safe=False)

@csrf_exempt
def momenlist(request):
    if request.method == 'GET':
        post = list(Momentum.objects.values())
        return JsonResponse(post, safe=False)

@csrf_exempt
def riskmomenlist(request):
    if request.method == 'GET':
        post = list(RiskMomentum.objects.values())
        return JsonResponse(post, safe=False)

@csrf_exempt
def valuelist(request):
    if request.method == 'GET':
        post = list(Value.objects.values())
        return JsonResponse(post, safe=False)

@csrf_exempt
def qualitylist(request):
    if request.method == 'GET':
        post = list(Quality.objects.values())
        return JsonResponse(post, safe=False)