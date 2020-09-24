from django.urls import path
from . import views
from django.urls import path,re_path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('lowvar', views.LowVariabilityView.as_view()),
    path('momen', views.MomentumView.as_view()),
    path('riskmomen', views.RiskMomentumView.as_view()),
    path('value', views.ValueView.as_view()),
    path('quality', views.QualityView.as_view()),
]