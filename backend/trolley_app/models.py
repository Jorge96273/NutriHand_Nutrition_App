from django.db import models
from profile_app.models import Profile
from recipe_app.models import Recipe
from food_app.models import Food

# Create your models here.

class Trolley(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="trolley")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="trolley")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="trolley")

