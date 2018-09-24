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
    email = forms.EmailField(label="Email address")
    email2 = forms.EmailField(label="Confirm Email")
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        }

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
            email_qs = User.objects.filter(email=email)
            if email_qs.exist():
                raise forms.ValidationError("This email has already been registered")
            if not "@" in email:
                raise forms.ValidationError("Please make sure you are using the correct conventions when filling out your email (example@gmail.com)")
            if not ".com" in email:
                raise forms.ValidationError("Please make sure you are using the correct conventions when filling out your email (example@gmail.com)")
    def clean_first_name(self):
                first_name = self.clean_data.get(first_name)
                first_name = re.search(r'[A-Za-z]', first_name)
    def clean_last_name(self):
                last_name = self.clean_data.get(last_name)
                last_name = re.search(r'[A-Za-z]',last_name)