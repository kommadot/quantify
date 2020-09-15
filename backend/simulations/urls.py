from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('simulation', views.SimulationList.as_view(),name='simulation'),
    url(r'^simulation/(?P<pk>[0-9]+)$', views.SimulationDetail.as_view()),
    path('simulationbreakdown', views.SimulationBreakdownList.as_view(),name='simulationbreakdown'),
    url(r'^simulationbreakdown/(?P<pk>[0-9]+)$', views.SimulationBreakdownDetail.as_view()),

    # path('google/', views.GoogleLogin.as_view(), name='google_login')
    # url(r'^simulations/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)