from django.db import models

class users(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    city =models.CharField(max_length=255)
