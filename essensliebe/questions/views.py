from django.shortcuts import render, Http404
from .models import Question, Answer
from .forms import UserResponseForm
# Create your views here.
def questions_view(request):
    if request.user.is_authenticated:
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            answer_id = form.cleaned_data.get('answer_id')
            question_id = form.cleaned_data.get('question_id')
            question_instance = Question.objects.get(id=question_id)
            answer_instance = Answer.objects.get(id=answer_id)
            print(answer_instance.text, question_instance.text)

        queryset = Question.objects.all().order_by('-timestamp')
        instance = queryset[0]
        context = {
            "form":form,
            #"queryset": queryset,
            "instance":instance
        }
        return render(request, "questions.html", context)
    else:
        raise Http404