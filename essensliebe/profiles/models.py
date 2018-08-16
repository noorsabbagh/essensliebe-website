from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    ethnicity = models.CharField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    picture = models.ImageField(upload_to="profile_image/", default="/media/profile_image/def_image.png")

def create_profile(sender, **kwargs):
	if kwargs ['created']:
	  profile = Profile.objects.create(user=kwargs ['instance'])
  
post_save.connect(create_profile,sender=User)

class PartnerPrefrences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Prefrences regarding partner's characteristics
    location = models.CharField(max_length=255, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    ethnicity = models.CharField(max_length=10, null=True, blank=True)

def create_partner_prefrences(sender, **kwargs):
    if kwargs ['created']:
        partner_prefrences = PartnerPrefrences.objects.create(user=kwargs ['instance'])
  
post_save.connect(create_partner_prefrences,sender=User)

class FoodPrefrences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Personal Dietry and food prefrences
    fav_food = models.CharField(max_length=255, null=True, blank=True)
    vegan = models.BooleanField(blank=True,null=True)
    vegetarian = models.BooleanField(blank=True,null=True)

def create_food_prefrences(sender, **kwargs):
    if kwargs ['created']:
        food_prefrences = FoodPrefrences.objects.create(user=kwargs ['instance'])
  
post_save.connect(create_food_prefrences,sender=User)