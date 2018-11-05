from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm, UserRegistrationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.http import HttpResponse
from faker import Faker
# Create your views here.
def register_view(request):
	#print(request.user.is_authenticated())
	title = "Register"
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		#new_user = authenticate(username=user.username, password=password)
		#login(request, new_user)
		return redirect('/login/')
	context = {
			"form":form,
			"title":title
	}
	return render(request, "form.html", context)

def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        return redirect('profile', username=request.user.username)
    return render(request, "form.html", {"form":form, "title": title})
	
def api_view(request):
	fake = Faker()
	for i in range(100):
		model = User(username = fake.user_name(),first_name = fake.first_name(),last_name = fake.last_name(),email = fake.email())
		model.set_password(fake.word()+fake.word()+fake.word())
		model.save()
	return HttpResponse(status=202)
	
def logout_view(request):
    logout(request)
    return redirect('/index/')
