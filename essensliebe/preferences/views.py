from django.shortcuts import render, Http404
from django.conf import settings
from django.contrib.auth.models import User
from .models import Questions
from .forms import UserResponseForm

# Create your views here.
def questions(request):
    if request.user.is_authenticated():
        form = UserResponseForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
        queryset = Questions.objects.all().order_by('-timestamp')
        instance = queryset[0]
        context = {
            "form":form,
            "instance":instance
        }
        return render(request, "questions.html", context)
    else:
        raise Http404 