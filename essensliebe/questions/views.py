from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Question, Answer
from .forms import UserResponseForm
# Create your views here.
def single(request, id):

    if request.user.is_authenticated:
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            #print(request.POST)
            answer_id = form.cleaned_data.get('answer_id')
            question_id = form.cleaned_data.get('question_id')
            question_instance = Question.objects.get(id=question_id)
            answer_instance = Answer.objects.get(id=answer_id)
            print(answer_instance.text, question_instance.text)
            next_q = Question.objects.all().order_by("?").first()
            return redirect("questions_single", id=next_q.id)

        queryset = Question.objects.all().order_by('-timestamp')
        instance = get_object_or_404(Question, id=id)
        context = {
            "form":form,
            #"queryset": queryset,
            "instance":instance
        }
        return render(request, "single.html", context)
    else:
        raise Http404

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
        instance = queryset[1]
        context = {
            "form":form,
            #"queryset": queryset,
            "instance":instance
        }
        return render(request, "questions.html", context)
    else:
        raise Http404