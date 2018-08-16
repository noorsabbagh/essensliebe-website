from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(max_length=3, null=True, blank=True)
    ethnicity = models.CharField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    picture = models.ImageField(upload_to="profile_image/", default="/media/profile_image/def_image.png")

def create_profile(sender, **kwargs):
	if kwargs ['created']:
	  profile = Profile.objects.create(user=kwargs ['instance'])
  
post_save.connect(create_profile,sender=User)