from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    favorite_food = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    picture = models.ImageField(upload_to="profile_images", null=True, blank=True)

  
