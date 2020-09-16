from django.urls import path

from . import views

urlpatterns = [
    path('google', views.GoogleLogin.as_view(), name='google_login'),
    # path('google/', obtain_jwt_token),
    path('kakao', views.KakaoLogin.as_view())
]