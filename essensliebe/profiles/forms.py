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
        
        def clean_age(self):
            age = self.cleaned_data.get('age')
            if not 18<= age >=112:
                raise forms.ValidationError ("Your age must be a identified by a number between 18 and 112")
            
            return age
        def clean_sex(self):
            sex = self.cleaned_data.get('sex')
            if not "male" or "female" or "other" in 'sex':
                    raise forms.ValidationError ("Your Sex must be identified in lower case male, female, or other")
            return sex
      

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
                
                    