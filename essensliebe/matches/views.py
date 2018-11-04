from django.shortcuts import render
from .models import Match
# Create your views here.
def matches_view(request):
    if request.user.is_authenticated:
        Match.objects.findMatches(request.user)
        matches = Match.objects.get_matches_with_percent(request.user)
        context = {
            "matches": matches,
        }
        return render(request, "matches_dashboard.html", context)
    return render(request, "index", context)