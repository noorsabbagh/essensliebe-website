from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .forms import EditProfileForm, EditPartnerPrefrencesForm, EditFoodPrefrencesForm
# Create your views here.
def profile(request):
    args = {'user':request.user}
    return render(request, 'profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form = EditProfileForm(instance=request.user.profile)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


def prefrences(request):
    return render(request, 'prefrences.html')

def edit_partner_prefrences(request):
    if request.method == 'POST':
        form = EditPartnerPrefrencesForm(data=request.POST or None, instance=request.user.partner_prefrences, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form = EditPartnerPrefrencesForm(instance=request.user.partner_prefrences)
        args = {'form': form}
        return render(request, 'edit_partner_prefrences.html', args)

def edit_food_prefrences(request):
    if request.method == 'POST':
        form = EditFoodPrefrencesForm(data=request.POST or None, instance=request.user.food_prefrences, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form = EditFoodPrefrencesForm(instance=request.user.food_prefrences)
        args = {'form': form}
        return render(request, 'edit_food_prefrences.html', args)