from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=50)
    trolley = models.ForeignKey("trolley_app.Trolley", on_delete=models.CASCADE, related_name= "foods", null= True)
    nutrition=models.TextField(max_length=200)

