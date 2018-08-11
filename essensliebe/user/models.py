from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    street = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name