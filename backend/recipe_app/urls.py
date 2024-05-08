from django.urls import path
from .views import Search_Nutrient
from .views import Search_Recipe
from .views import A_Recipe

urlpatterns = [
    path('search_nutrient/<str:nutrient>/', Search_Nutrient.as_view(), name="search_nutrient"),
    path('search_recipe/<str:recipe>/', Search_Recipe.as_view(), name="search_recipe"),
    path('<str:recipe>/', A_Recipe.as_view(), name="delete_recipe"),
    path('', A_Recipe.as_view(), name="A_Recipe"),

]

