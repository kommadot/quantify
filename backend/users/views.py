from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
from django.http import HttpResponse
from .models import User
import json
import jwt
from .serializers import UserSerializer
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# @permission_classes((IsAuthenticated,))
# @authentication_classes((JSONWebTokenAuthentication,))


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    def post(self, request):
        print(request.data['access_token'])
        google_access_token = request.data['access_token']
        url = 'https://www.googleapis.com/oauth2/v3/userinfo'
        headers = {'Authorization' : f'Bearer {google_access_token}'}
        google_response = requests.get(url, headers=headers)
        json_data = json.loads(google_response.text)
        print(json_data)
        
        u = User.objects.filter(social_id=json_data['sub'])
        print(len(u))
        if not u:
            user = User(nickname=json_data['email'].split('@')[0], social_id=json_data['sub'], platform='google')
            user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        user = User.objects.get(pk = u[0].id)
        user.social_id = 0
        return Response(UserSerializer(user).data, status=status.HTTP_400_BAD_REQUEST)


class KakaoLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    def post(self, request):
        print("asdf")
        url = "https://kapi.kakao.com/v2/user/me"
        json_data = json.loads(requests.get(url,headers={'Authorization':'Bearer '+request.data['access_token']}).text)
        u = User.objects.filter(social_id=json_data['id'])
        print(len(u))
        if not u:
            # user = User(nickname="asas", social_id=json_data['id'], platform='kakao')
            user = User(nickname=json_data['properties']['nickname'], social_id=json_data['id'], platform='kakao')
            user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        user = User.objects.get(pk = u[0].id)
        user.social_id = 0
        return Response(UserSerializer(user).data, status=status.HTTP_400_BAD_REQUEST)