from django.urls import path

from . import views

urlpatterns = [
    path('google', views.GoogleLogin.as_view()),
    path('kakao', views.KakaoLogin.as_view()),
    # path('google/', obtain_jwt_token),
]