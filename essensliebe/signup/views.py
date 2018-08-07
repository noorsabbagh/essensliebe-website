from django.shortcuts import render
from django.template import loader

# Create your views here.
def signup(request):
    return render(request, 'signup/signup.html')