from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
import requests 
from .models import Recipe
from requests_oauthlib import OAuth1
from backend_project.settings import env
from pprint import PrettyPrinter
from trolley_app.models import Trolley
from profile_app.views import Authorizations
from food_app.views import Food

class Trolley_Items(Authorizations):

    def get(self, request):
        recipes = Recipe.objects.all()  
        foods = Food.objects.all()
        recipe_names = [recipe.name for recipe in recipes] 
        food_names = [food.name for food in foods]
        recipe_food = recipe_names + food_names
        return Response(recipe_food, status= HTTP_200_OK)  