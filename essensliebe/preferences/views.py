from django.shortcuts import render, Http404
from django.conf import settings
from django.contrib.auth.models import User
from .models import Questions, UserAnswer, Answer
from .forms import UserResponseForm

# Create your views here.
def questions(request):
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            questions_id = form.cleaned_data.get('questions_id')
            answer_id = form.cleaned_data.get('answer_id')
            question_instance = Questions.objects.get(id=questions_id)
            answer_instance = Answer.objects.get(id=answer_id)
            
            new_user_answer = UserAnswer()
            new_user_answer.question = question_instance
            new_user_answer.user = request.user
            new_user_answer.answer = Answer.objects.get(id=answer_id)

            new_user_answer.save()

        queryset = Questions.objects.all().order_by('-timestamp')
        instance = queryset[0]
        context = {
            "form":form,
            "instance":instance
        }
        return render(request, "questions.html", context)
    else:
        raise Http404 