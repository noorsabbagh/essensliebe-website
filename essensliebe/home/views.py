from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from matches.models import Match



# Create your views here.
def index(request):
    return render(request, 'home/index.html')
	
def matches_view(request):
    if request.user.is_authenticated:
        matches = Match.objects.get_matches_with_percent(request.user)
        context = {
            "matches": matches,
        }
        return render(request, "index.html", context)
    return render(request, "index", context)