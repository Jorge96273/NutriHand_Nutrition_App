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
from requests_oauthlib import OAuth1
from backend_project.settings import env
from pprint import PrettyPrinter
from profile_app.views import Authorizations
from trolley_app.models import Trolley
from .models import Food

import json


pp = PrettyPrinter(indent=2, depth=2)


class Search_Foods(Authorizations):

    def get(self, request, food):
        print('in the get method')
        api_key = env.get("API_KEY")
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/search"

        querystring = {"query": food, "number": "10"}

        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        json_response = response.json()
        print(json_response)
        response_list = []
        for x in json_response['products']:
            print(x)
            info = {}
            info["Title"] = x.get('title')
            info["id"] = x.get('id')
            info["image"] = x.get('image')
            response_list.append(info)
        return Response(response_list, status = HTTP_200_OK) 
    
    def post(self, request):
        request_data = json.loads(request.body.decode('utf-8'))
        food_name = request_data.get('food')
        user = request.user 
        food, _ = Food.objects.get_or_create(name=food_name)
        trolley = Trolley.objects.get(profile=user)

        trolley.add_food(food)

        return Response(f"{food.name} has been added to your cart", status = HTTP_201_CREATED)
    
   

    def delete(self, request, food):
        
        try:
            trolley = Trolley.objects.get(profile=request.user)
        except Trolley.DoesNotExist:
            return Response(status= HTTP_400_BAD_REQUEST)

        found_food = trolley.foods.filter(name=food).first()

        if found_food:
            trolley.foods.remove(found_food)
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
        

