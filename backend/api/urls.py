from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('auth/', include('users.urls')),
    path('strategy/', include('strategy.urls')),
    path('simulations/',include('simulations.urls')),
]
