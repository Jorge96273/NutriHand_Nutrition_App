from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=50)
    nutrition=models.TextField(max_length=200)