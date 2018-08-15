from django.contrib import admin
from .models import Questions, Answer, UserAnswer
# Register your models here.
admin.site.register(Questions)
admin.site.register(UserAnswer)
admin.site.register(Answer)
