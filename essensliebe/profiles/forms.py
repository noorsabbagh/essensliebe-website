from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserChangeForm

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'location',
            'sex',
            'age',
            'ethnicity',
            'description',
            'picture'

        )
        exclude = (
            'password',
            'username'
        )
    