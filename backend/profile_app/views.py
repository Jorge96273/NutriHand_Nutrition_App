from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import(
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .models import Profile
from trolley_app.models import Trolley
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
from .serializer import ProfileSerializer


class Signup(APIView):
    def post(self, request):
        data = request.data.copy()
        data['username'] = request.data.get("username", data.get("email"))
        new_profile = Profile(**data)
        try:
            new_profile.full_clean()
            new_profile.save()
            new_profile.set_password(data.get("password"))
            new_profile.save()
            Trolley.objects.create(profile=new_profile)
            token = Token.objects.create(user = new_profile)
            return Response({"profile":new_profile.email,"token":token.key}, status=HTTP_201_CREATED)
        except ValidationError as e:
            print(e)
            return Response(e, status=HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        data=request.data.copy()
        data['username']=request.data.get("username", data.get("email"))
        a_user = authenticate(username=data.get("username"),password=data.get("password"))
        print("A USER ", a_user)
        if a_user:
            login(request,a_user)
            token, created= Token.objects.get_or_create(user = a_user)
            return Response({"profile":a_user.username,"token":token.key}, status= HTTP_200_OK)
        return Response("No user matching credentials", status=HTTP_400_BAD_REQUEST)
    

class Authorizations(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

class Logout(Authorizations):
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=HTTP_204_NO_CONTENT)
    
class Info(Authorizations):
    def get (self, request):
        profile = ProfileSerializer(request.user)
        return Response(profile.data ,HTTP_200_OK)
        



