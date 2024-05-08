from django.db import models


class Recipe(models.Model):
    name = models.CharField(default="Recipe", unique=True, max_length=50)
    ingredients= models.TextField(default="n/a")
    nutrients= models.TextField(default="n/a")
    trolley = models.ForeignKey('trolley_app.Trolley', on_delete=models.CASCADE, related_name='recipes', null=True)
