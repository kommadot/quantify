from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
import requests
from django.http import HttpResponse
# from django.views.generic import View

class GoogleLogin(SocialLoginView):
# class GoogleLogin(View):
    adapter_class = GoogleOAuth2Adapter
    def post(self, request):
        print(request.data['access_token'])
        google_access_token = request.data['access_token']
        url = 'https://www.googleapis.com/oauth2/v3/userinfo'
        headers = {'Authorization' : f'Bearer {google_access_token}'}
        google_response = requests.get(url, headers=headers)
        return HttpResponse(f'{google_response.text}')