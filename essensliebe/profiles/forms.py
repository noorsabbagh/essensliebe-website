from django import forms
from django.contrib.auth.models import User
from .models import Profile, PartnerPrefrences, FoodPrefrences
from django.contrib.auth.forms import UserChangeForm
from directmessage.models import DirectMessage

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
      

class EditPartnerPrefrencesForm(forms.ModelForm):
    class Meta:
        model = PartnerPrefrences
        fields = (
            'location',
            'sex',
            'age',
            'ethnicity'
        )

class EditFoodPrefrencesForm(forms.ModelForm):
    class Meta:
        model = FoodPrefrences
        fields = (
            'fav_food',
            'vegan',
            'vegetarian'
        )
