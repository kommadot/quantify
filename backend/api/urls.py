from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from . import views
urlpatterns = [
    path('auth/', include('users.urls')),
    path('strategy/', include('strategy.urls')),
    path('simulations/',include('simulations.urls')),
    path('community/',include('community.urls')),
    path('backtest/',include('backtest.urls')),
    path('login/', obtain_jwt_token),
    re_path(r'^price/(?P<code>[0-9]+)$',views.Price.as_view()),
    re_path(r'^beforeprice/(?P<code>[0-9]+)$',views.BeforePrice.as_view()),
    re_path(r'^stockprice/(?P<code>[\w\-]+)$',views.StockPriceDetail.as_view()),
    path('company',views.CompanyAll.as_view()),
]
