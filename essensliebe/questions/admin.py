from django.contrib import admin
from .models import Question, Answer, UserAnswer
# Register your models here.
class AnswerTabularInLine(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerTabularInLine]
    class Meta:
        model = Question

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(UserAnswer)