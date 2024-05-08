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
from .serializers import RecipeSerializer
from requests_oauthlib import OAuth1
from backend_project.settings import env
from pprint import PrettyPrinter
from trolley_app.models import Trolley
from profile_app.views import Authorizations

import json

pp = PrettyPrinter(indent=2, depth=2)


class A_Recipe(Authorizations):

    def get(self, request, recipe):
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"
        querystring = querystring = {"query":recipe,"number":"1","limitLicense":"false","ranking":"2"}
        api_key = env.get("API_KEY")
        headers = {
	        "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        response_json = response.json()
        results = response_json.get('results', [])
        name = results[0].get('title') if results else None
        print(name)
        # name = get_object_or_404(Recipe, name = name)
        print(f"\n{name}\n")
        # serialized = RecipeSerializer(response_json)
        # return Response(serialized.data, HTTP_200_OK)
        
        return Response(response_json)
    
    def post(self, request):
        request_data = json.loads(request.body.decode('utf-8'))
        recipe_name = request_data.get('recipe')
        print("REQUEST BODY ", recipe_name)
        user = request.user
        print("LOGIN USER ", user)
        recipe, _ = Recipe.objects.get_or_create(name=recipe_name)
        trolley = Trolley.objects.get(profile=user)

        
        trolley.add_recipe(recipe)

        return Response(f"{recipe.name} has been added to your cart", status = HTTP_201_CREATED)
   

    def delete(self, request, recipe):
        trolley = Trolley.objects.get(profile=request.user)
        found_recipe = trolley.recipes.filter(name=recipe).first()
        if found_recipe:
            trolley.remove_recipe(found_recipe)
            return Response(status= HTTP_204_NO_CONTENT)
        else:
            return Response(status= HTTP_400_BAD_REQUEST)

class Search_Nutrient(APIView):
    def get(self, request, nutrient):
        nutrient = nutrient[0].upper() + nutrient[1:]
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByNutrients"
        querystring = {"limitLicense":"true",f"min{nutrient}":"20"}
        api_key = env.get("API_KEY")
        api_host = env.get("API_HOST")
        headers = {
	        "X-RapidAPI-Key": api_key,
	        "X-RapidAPI-Host": api_host
        }
        response = requests.get(url, headers=headers, params=querystring)
        json_response = response.json()
        print(json_response)
        nutrient = nutrient[0].lower() + nutrient[1:]
        response_list = []
        for x in json_response:
            print(x)
            info = {}
            info["Title"] = x.get('title')
            info[f"{nutrient}"] = x.get(f'{nutrient}')
            info["calories"] = x.get('calories')
            info["protein"] = x.get('protein')
            info["fat"] = x.get('fat')
            info["carbs"] = x.get('carbs')
            info["iron"] = x.get('iron')
            info["vitaminC"] = x.get('vitaminC')
            info["id"] = x.get('id')
            info["image"] = x.get('image')
            response_list.append(info)
        return Response(response_list, status = HTTP_200_OK) 
 

class Search_Recipe(APIView):
    def get(self, request, recipe):
            url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

            querystring = {"query":recipe}
            api_key = env.get("API_KEY")

            headers = {
                "X-RapidAPI-Key": api_key,
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            json_response = response.json()
            return Response(json_response)
        


