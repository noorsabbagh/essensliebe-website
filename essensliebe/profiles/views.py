from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from likes.models import UserLike
from matches.models import Match
from .forms import EditProfileForm, EditPartnerPrefrencesForm, EditFoodPrefrencesForm
# Create your views here.
User = get_user_model()

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    matches, match_created = Match.objects.get_or_create_match(user_a=request.user, user_b=user)
    profile, created = Profile.objects.get_or_create(user=user)
    user_like, user_like_created = UserLike.objects.get_or_create(user=request.user)
    do_i_like = False
    if user in user_like.liked_users.all():
        do_i_like=True
    mutual_like = user_like.get_mutual_like(user)
    args = {
        'profile':profile, 
        'matches':matches,
        "mutual_like": mutual_like,
        "do_i_like": do_i_like,
    }
    return render(request, 'profile.html', args)
    

def edit_profile(request, username):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/profile/' + str(username))

    else:
        form = EditProfileForm(instance=request.user.profile)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


def prefrences(request, username):
    return render(request, 'prefrences.html')

def edit_partner_prefrences(request, username):
    if request.method == 'POST':
        form = EditPartnerPrefrencesForm(data=request.POST or None, instance=request.user.partner_prefrences, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/profile',)

    else:
        form = EditPartnerPrefrencesForm(instance=request.user.partner_prefrences)
        args = {'form': form}
        return render(request, 'edit_partner_prefrences.html', args)

def edit_food_prefrences(request, username):
    if request.method == 'POST':
        form = EditFoodPrefrencesForm(data=request.POST or None, instance=request.user.food_prefrences, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form = EditFoodPrefrencesForm(instance=request.user.food_prefrences)
        args = {'form': form}
        return render(request, 'edit_food_prefrences.html', args)