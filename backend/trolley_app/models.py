from django.db import models
from profile_app.models import Profile
from recipe_app.models import Recipe
from food_app.models import Food

# Create your models here.

class Trolley(models.Model):
    quantity= models.PositiveIntegerField(default=0)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="trolley")

    def add_recipe(self, recipe):
        self.recipes.add(recipe)
        self.save()

    def add_food(self, food):
        self.foods.add(food)
        self.save()

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)
        self.save()


    def remove_food(self, recipe):
        self.food.remove(recipe)
        self.save()