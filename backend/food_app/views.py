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



class Search_Foods(APIView):

    def get(self, request, food):
        url = "https://dietagram.p.rapidapi.com/apiFood.php"
        querystring = {"name":"apple","lang":"en"}
        api_key = env.get("API_KEY")
        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "dietagram.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        json_response = response.json()
        response_list = []
        print(response)
        print(json_response)
        for x in response:
            print(x)
            info = {}
            info["name"] = x.get('name')
            info["caloric"] = x.get('caloric')
            info["protein"] = x.get('protein')
            info["fat"] = x.get('fat')
            response_list.append(info)
        return Response(response_list,HTTP_200_OK) 
    
# [
#   "{\"dishes\":[{\"id\":\"2410\",\"name\":\"Apple\",\"caloric\":\"52\",\"type\":\"x\",\"fat\":\"0.17\",\"carbon\":\"13.8\",\"protein\":\"0.26\",\"category_id\":\"50",
#   "0\"},{\"id\":\"2407\",\"name\":\"Apples\",\"caloric\":\"52\",\"type\":\"x\",\"fat\":\"0.17\",\"carbon\":\"13.8\",\"protein\":\"0.26\",\"category_id\":\"500\"},{\"",
#   "id\":\"789\",\"name\":\"Apple Pie\",\"caloric\":\"240\",\"type\":\"s\",\"fat\":\"13\",\"carbon\":\"29\",\"protein\":\"2\",\"category_id\":\"17\"},{\"id\":\"28\",\"n",
#   "ame\":\"Apple, raw\",\"caloric\":\"52\",\"type\":\"f\",\"fat\":\"0.3\",\"carbon\":\"12.9\",\"protein\":\"0.3\",\"category_id\":\"1\"},{\"id\":\"2397\",\"name\":\"",
#   "Applesauce\",\"caloric\":\"76\",\"type\":\"x\",\"fat\":\"0.18\",\"carbon\":\"19.9\",\"protein\":\"0.18\",\"category_id\":\"500\"},{\"id\":\"2402\",\"name\":\"Ap",
#   "ple Cider\",\"caloric\":\"47\",\"type\":\"x\",\"fat\":\"0.11\",\"carbon\":\"11.6\",\"protein\":\"0.06\",\"category_id\":\"500\"},{\"id\":\"2688\",\"name\":\"App",
#   "le Chips\",\"caloric\":\"460\",\"type\":\"x\",\"fat\":\"21.6\",\"carbon\":\"73.7\",\"protein\":\"1.04\",\"category_id\":\"500\"},{\"id\":\"2689\",\"name\":\"App",
#   "le Juice\",\"caloric\":\"47\",\"type\":\"x\",\"fat\":\"0.11\",\"carbon\":\"11.6\",\"protein\":\"0.06\",\"category_id\":\"500\"},{\"id\":\"4225\",\"name\":\"Rose",
#   "-Apples\",\"caloric\":\"25\",\"type\":\"x\",\"fat\":\"0.30\",\"carbon\":\"5.70\",\"protein\":\"0.60\",\"category_id\":\"500\"},{\"id\":\"5233\",\"name\":\"Dried",
#   " Apple\",\"caloric\":\"243\",\"type\":\"x\",\"fat\":\"0.32\",\"carbon\":\"65.8\",\"protein\":\"0.93\",\"category_id\":\"500\"},{\"id\":\"21\",\"name\":\"Dried A",
#   "pples\",\"caloric\":\"255\",\"type\":\"f\",\"fat\":\"0.3\",\"carbon\":\"65.9\",\"protein\":\"0.9\",\"category_id\":\"1\"},{\"id\":\"2406\",\"name\":\"Apple Bana",
#   "na\",\"caloric\":\"89\",\"type\":\"x\",\"fat\":\"0.33\",\"carbon\":\"22.8\",\"protein\":\"1.09\",\"category_id\":\"500\"},{\"id\":\"10682\",\"name\":\"Apple, dr",
#   "ied\",\"caloric\":\"294\",\"type\":\"x\",\"fat\":\"1.3\",\"carbon\":\"68\",\"protein\":\"0.3\",\"category_id\":\"500\"},{\"id\":\"12862\",\"name\":\"Apple Chips",
#   "\\n\",\"caloric\":\"460\",\"type\":\"x\",\"fat\":\"21.6\",\"carbon\":\"73.6\",\"protein\":\"1.03\",\"category_id\":\"555\"},{\"id\":\"13544\",\"name\":\"Dried Ap",
#   "ple\\n\",\"caloric\":\"243\",\"type\":\"x\",\"fat\":\"0.30\",\"carbon\":\"64.0\",\"protein\":\"0.91\",\"category_id\":\"555\"}]}"
# ]






# ,"minProtein":"0","minVitaminC":"0","minSelenium":"0","maxFluoride":"50","maxVitaminB5":"50","maxVitaminB3":"50","maxIodine":"50","minCarbs":"0","maxCalories":"250","minAlcohol":"0","maxCopper":"50","maxCholine":"50","maxVitaminB6":"50","minIron":"0","maxManganese":"50","minSodium":"0","minSugar":"0","maxFat":"20","minCholine":"0","maxVitaminC":"50","maxVitaminB2":"50","minVitaminB12":"0","maxFolicAcid":"50","minZinc":"0","offset":"0","maxProtein":"100","minCalories":"0","minCaffeine":"0","minVitaminD":"0","maxVitaminE":"50","minVitaminB2":"0","minFiber":"0","minFolate":"0","minManganese":"0","maxPotassium":"50","maxSugar":"50","maxCaffeine":"50","maxCholesterol":"50","maxSaturatedFat":"50","minVitaminB3":"0","maxFiber":"50","maxPhosphorus":"50","minPotassium":"0","maxSelenium":"50","maxCarbs":"100","minCalcium":"0","minCholesterol":"0","minFluoride":"0","maxVitaminD":"50","maxVitaminB12":"50","minIodine":"0","maxZinc":"50","minSaturatedFat":"0","minVitaminB1":"0","maxFolate":"50","minFolicAcid":"0","maxMagnesium":"50","minVitaminK":"0","maxSodium":"50","maxAlcohol":"50","maxCalcium":"50","maxVitaminA":"50","maxVitaminK":"50","minVitaminB5":"0","maxIron":"50","minCopper":"0","maxVitaminB1":"50","number":"10","minVitaminA":"0","minPhosphorus":"0","minVitaminB6":"0","minFat":"5","minVitaminE":"0"}

