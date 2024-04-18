from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
import requests 
from requests_oauthlib import OAuth1

class All_Foods(APIView):

    def get(self, request):
        
        return Response("helllllllo",HTTP_200_OK) 