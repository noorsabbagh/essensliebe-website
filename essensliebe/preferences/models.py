from django.db import models
from django.conf import settings

# Create your models here.
class Questions(models.Model):
    text = models.TextField()
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.OneToOneField(Questions, on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.text

class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer