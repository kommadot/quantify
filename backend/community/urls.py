from django.urls import path, re_path
from . import views


urlpatterns = [
    path('community', views.CommunityList.as_view()),
    re_path(r'^community/(?P<article_pk>[0-9]+)$', views.CommunityDetail.as_view()), 
]
