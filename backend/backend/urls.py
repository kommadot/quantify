from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),

    path('login/', obtain_jwt_token),
]
