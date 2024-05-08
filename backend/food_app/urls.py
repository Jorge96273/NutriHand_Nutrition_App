from django.urls import path
from .views import Search_Foods

urlpatterns = [
    path('search_food/<str:food>/', Search_Foods.as_view(), name="search_foods"),
    path('<str:food>/', Search_Foods.as_view(), name="delete_recipe"),
    path('', Search_Foods.as_view(), name="A_Recipe"),
]
