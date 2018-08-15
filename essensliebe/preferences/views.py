from django.shortcuts import render, Http404
from django.conf import settings
from django.contrib.auth.models import User
from .models import Questions
# Create your views here.
def questions(request):
    if request.user.is_authenticated():
        queryset = Questions.objects.all().order_by('-timestamp')
        context = {
            "queryset": queryset
        }
        return render(request, "questions.html", context)
    else:
        raise Http404