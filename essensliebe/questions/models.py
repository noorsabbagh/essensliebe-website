from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    text = models.TextField()
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return(self.text)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return(self.text)


LEVELS = (
        ('Mandatory', 'Mandatory'),
        ('Very Important', 'Very Important'),
        ('Somewhat Important', 'Somewhat Important'),
        ('Not Important', 'Not Importan'),
        )

class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    my_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='user_answer')
    my_answer_importance = models.CharField(max_length=50, choices=LEVELS)
    my_points = models.IntegerField(default=-1)
    their_answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE, related_name='match_answer')
    their_importance = models.CharField(max_length=50, choices=LEVELS)
    their_points = models.IntegerField(default=-1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.my_answer.text

def score_importance(importance_level):
    if importance_level == "Mandatory":
        points = 300
    elif importance_level == "Very Important":
        points = 200
    elif importance_level == "Somewhat Important":
        points = 50
    elif importance_level == "Not Important":
        points = 0
    else:
        points = 0
    return points