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
		if age is None or not 18<= age and not age >=112:
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

	age = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9 ]+', 'title':'Enter Characters Only '}))
	sex = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
	location = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[\w ]+', 'title':'Enter Characters Only '}))
	ethnicity = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
	def clean(self):
		form_data = self.cleaned_data
		age = self.cleaned_data.get('age')
		sex = self.cleaned_data.get('sex')
		location = self.cleaned_data.get('location')
		ethnicity = self.cleaned_data.get('ethnicity')
		if age is None or not 18 < age < 112:
			self.errors["age"] = ["Your age must be a identified by a number between 18 and 112"]
		if sex is None:
			self.errors["sex"] = ["Your Sex must be identified in lower case male, female, or other"]
		return form_data
		if location is None:
			self.errors["location"] = ["Make your location a valid address e.g 35 Swanston Street Melbourne"]
		return form_data
		if ethnicity is None:
			self.errors["ethnicity"] = ["Ensure you enter a valid Race you belong to"]
		return form_data
	class Meta:
		model = PartnerPrefrences
		fields = {
            'location',
            'sex',
            'age',
            'ethnicity'
        }




class EditFoodPrefrencesForm(forms.ModelForm):
	

	fav_food = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
	vegan  = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
	vegetarian = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
	def clean(self):
		form_data = self.cleaned_data
		fav_food = self.cleaned_data.get('fav_food')
		vegan = self.cleaned_data.get('vegan')
		vegetarian= self.cleaned_data.get('vegetarian')
		if fav_food is None:
			self.errors["fav_food"] = ["Please make sure you select a favorite food"]
		return form_data
		if vegan is None:
			self.errors["vegan"] = ["Please make sure your are either vegan or not"]
		return form_data
		if vegetarian is None:
			self.errors["vegetarian"] = ["Please make sure you are either vegetarian or not"]
		return form_data
	
	
	
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
        #def clean_ethnicity(self):
                #ethnicity = self.clean_data.get(ethnicity)
                #ethnicity = re.search('[A-Za-z]', ethnicity)
                
                    