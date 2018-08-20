from django.shortcuts import render, Http404
from .models import Question
# Create your views here.
def questions_view(request):
    if request.user.is_authenticated():
        queryset = Question.objects.all().order_by('-timestamp')
        context = {
            "queryset": queryset
        }
        return render(request, "questions.html", context)
    else:
        raise Http404