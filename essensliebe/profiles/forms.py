from django import forms
from django.contrib.auth.models import User
from .models import Profile, PartnerPrefrences, FoodPrefrences
from django.contrib.auth.forms import UserChangeForm
from directmessage.models import DirectMessage
import re

class EditProfileForm(forms.ModelForm):
		
	age = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9 ]+', 'title':'Enter Characters Only '}))
	sex = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
	location = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[\w ]+', 'title':'Enter Characters Only '}))
	def clean(self):
		form_data = self.cleaned_data
		age = self.cleaned_data.get('age')
		sex = self.cleaned_data.get('sex')
		if age is None or 18<= age >=112:
			self.errors["age"] = ["Your age must be a identified by a number between 18 and 112"]
		if sex is None:
			self.errors["sex"] = ["Your Sex must be identified in lower case male, female, or other"]
		return form_data
      
	class Meta:
		model = Profile
		fields = {
            'location',
            'sex',
            'age',
            'ethnicity',
            'description',
            'picture'
		}   
		
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

        

    
			    
                
      #  def clean_location(self):
       #         location = self.clean_data.get(location)
        #        re.search('[A-Za-z]', location)
        #            raise forms.ValidationError ("Location must only use Letters no characters")
		#	    return location 
        def clean_ethnicity(self):
                ethnicity = self.clean_data.get(ethnicity)
                ethnicity = re.search('[A-Za-z]', ethnicity)
                
                    