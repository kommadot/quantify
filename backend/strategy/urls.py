from django.urls import path
from . import views

urlpatterns = [
    path('getlowvar/', views.lowvarlist),
    path('getmomen/', views.momenlist),
    path('getriskmomen/', views.riskmomenlist),
]