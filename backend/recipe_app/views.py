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

pp = PrettyPrinter(indent=2, depth=2)

class Search_Nutrient(APIView):
    # first letter of nutrient has to be capital 
    def get(self, request, nutrient):
        nutrient = nutrient[0].upper() + nutrient[1:]
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByNutrients"
        querystring = {"limitLicense":"true",f"min{nutrient}":"15"}
        api_key = env.get("API_KEY")
        api_host = env.get("API_HOST")
        headers = {
	        "X-RapidAPI-Key": api_key,
	        "X-RapidAPI-Host": api_host
        }
        response = requests.get(url, headers=headers, params=querystring)
        json_response = response.json()
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
        




        # pp.pprint(json_response[0].get('title'))

        #          {
        #     "id": 639891,
        #     "title": "Coffee-braised Short Ribs",
        #     "image": "https://img.spoonacular.com/recipes/639891-312x231.jpg",
        #     "imageType": "jpg",
        #     "calories": 877,
        #     "protein": "74g",
        #     "fat": "42g",
        #     "carbs": "45g",
        #     "iron": "20mg"
        #   },
