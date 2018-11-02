from django import forms
#from user.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
import re
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect pasword")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
    
	first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Letters Only '}))
	last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Letters Only '}))
	password = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'type':'password','max_length': '20', 'min_length': '6', 'autocomplete': 'off','pattern':'[A-z0-9 ]+', 'title':'Enter Letters and numbers only '}))
	email = forms.EmailField(label="Email address")
	email2 = forms.EmailField(label="Confirm Email")
		
	def clean(self):
		form_data = self.cleaned_data
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		password = self.cleaned_data.get('password')
		if password is not None and len(password) < 6:
			self.errors["password"] = ["Passwords must be between 6-20 Characters"]
		if email is None or email2 is None:
			self.errors["email"] = ["Must fill in email"]
		else:
			if email != email2:
				self.errors["email"]=["Emails must match"]
			if User.objects.filter(email = email).count() > 0:
				self.errors["email"]=["This email has already been registered"]
			if not "@" in email:
				self.errors["email"]=["Please make sure you are using the correct conventions when filling out your email (example@gmail.com)"]
		return form_data
		
	class Meta:
		model = User
		fields = {
            'first_name',
             'last_name',
            'username',
            'email',
            'password'
        }      