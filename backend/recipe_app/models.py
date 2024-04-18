from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(default="Recipe", unique=True, max_length=50)
    ingredients= models.TextField(default="n/a")
    nutrients= models.TextField(default="n/a")
