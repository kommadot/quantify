from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
from django.forms.models import model_to_dict
from django.http import HttpResponse
from .models import User
import json
import jwt
from .serializers import UserSerializer,UserSerializerWithToken
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# @permission_classes((IsAuthenticated,))
# @authentication_classes((JSONWebTokenAuthentication,))


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    def post(self, request):
        
        google_access_token = request.data['access_token']
        url = 'https://www.googleapis.com/oauth2/v3/userinfo'
        headers = {'Authorization' : f'Bearer {google_access_token}'}
        google_response = requests.get(url, headers=headers)
        json_data = json.loads(google_response.text)
        u = User.objects.filter(social_id=json_data['sub'])
        if not u:
            user = User(username=json_data['email'].split('@')[0], social_id=json_data['sub'], platform='google',password=json_data['sub'])
            serializer = UserSerializerWithToken(data = model_to_dict(user))
            if serializer.is_valid():
                serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        user = User.objects.get(pk = u[0].id)
        user.social_id = 0
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)


class KakaoLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    def post(self, request):
        url = "https://kapi.kakao.com/v2/user/me"
        json_data = json.loads(requests.get(url,headers={'Authorization':'Bearer '+request.data['access_token']}).text)
        u = User.objects.filter(social_id=json_data['id'])
        if not u:
            user = User(username=json_data['properties']['nickname'], social_id=json_data['id'], platform='kakao',password=json_data['id'])
            serializer = UserSerializerWithToken(data = model_to_dict(user))
            if serializer.is_valid():
                serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        user = User.objects.get(pk = u[0].id)
        user.social_id = 0
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
    
    
