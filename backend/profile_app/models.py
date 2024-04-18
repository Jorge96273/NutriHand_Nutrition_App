from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Profile(AbstractUser):
    bio = models.CharField(blank=True, max_length=100)
    
