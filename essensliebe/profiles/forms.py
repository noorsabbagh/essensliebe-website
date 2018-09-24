from django import forms
from django.contrib.auth.models import User
from .models import Profile, PartnerPrefrences, FoodPrefrences
from django.contrib.auth.forms import UserChangeForm
from directmessage.models import DirectMessage
import re
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

    
        def clean_age(self):
		        age = self.cleaned_data.get(age)
		        if not 18<= age <=112:
		            raise forms.ValidationError ("Your age must be a identified by a number between 18 and 112")

        def clean_sex(self):
                sex = self.clean_data.get(sex)
                if not "male" or "female" or "other" in sex:
                    raise forms.ValidationError ("Your Sex must be identified in lower case male, female, or other")  
        def clean_location(self):
                location = self.clean_data.get(location)
                location = re.search(r'[A-Za-z]', location)
        def clean_ethnicity(self):
                ethnicity = self.clean_data.get(ethnicity)
                ethnicity = re.search(r'[A-Za-z]', ethnicity)
                
                    