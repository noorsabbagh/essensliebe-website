from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .forms import EditProfileForm
# Create your views here.
def profile(request):
    args = {'user':request.user}
    return render(request, 'profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST or None, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form = EditProfileForm(instance=request.user.profile)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)
