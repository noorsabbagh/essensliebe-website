from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    city =models.CharField(max_length=255)

    def __str__(self):
        return self.firstname + " " + self.lastname

    