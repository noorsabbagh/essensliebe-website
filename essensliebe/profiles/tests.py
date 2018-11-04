from django.test import TestCase
from django.contrib.auth.models import User
from .models import PartnerPrefrences, FoodPrefrences
from .forms import *

class TestEditProfile(TestCase):
    def test_edit_profile_valid(self):
        self.user = User.objects.create_user(username='testuser', password='12345', first_name='nick', last_name='lim', email='ni@gmail.com')
        login = self.client.login(username='testuser', password='12345')
        data = {'location': 'RMIT',
                'sex': 'Male',
                'age': 11,
                'ethnicity': 'Asian',
                'description': 'Hi',
                'picture': None,
                }
class Setup_Class(TestCase):
	
	def setUp(self):
		self.user = User.objects.create(username="testyMcTesty" ,password="pass1234")

    def test_edit_profile_invalid(self):
        self.user = User.objects.create_user(username='testuser', password='12345', first_name='nick', last_name='lim', email='ni@gmail.com')
        login = self.client.login(username='testuser', password='12345')
        data = {'location': 'RMIT',
                'sex': 999,
                'age': 'ABC!@#',
                'ethnicity': 'Asian',
                'description': 'Hi',
                'picture': None,
                }
        
        profile = "/profile/" + self.user.username + "/edit/"
        response = self.client.post(profile, data, follow=True)
        self.assertTrue(response.request["PATH_INFO"].startswith('/profile/'))

		
class UserPreferencesForm_Test(TestCase):
	
	def test_UserPreferencesForm_valid(self):
		 form = EditPartnerPrefrencesForm(data={"location":"35 boronia road boronia","sex":"male","age":"24","ethnicity":"white"})
		 self.assertTrue(form.is_valid())

	def test_UserPreferencesForm_Invalid_Age_Young(self):
		 form = EditPartnerPrefrencesForm(data={"location":"35 boronia road boronia","sex":"male","age":"2"})
		 self.assertFalse(form.is_valid())	 

	def test_UserPreferencesForm_Invalid_Age_Old(self):
		 form = EditPartnerPrefrencesForm(data={"location":"35 boronia road boronia","sex":"male","age":"260"})
		 self.assertFalse(form.is_valid())
		
	def test_UserPreferencesForm_Missing_Age(self):
		 form = EditPartnerPrefrencesForm(data={"location":"35 boronia road boronia","sex":"male","age":""})
		 self.assertFalse(form.is_valid())
		 
	def test_UserPreferencesForm_Missing_Sex(self):
		 form = EditPartnerPrefrencesForm(data={"location":"35 boronia road boronia","sex":"","age":"21"})
		 self.assertFalse(form.is_valid())
		 
	def test_UserPreferencesForm_Missing_Location(self):
		 form = EditPartnerPrefrencesForm(data={"location":"","sex":"male","age":"21"})
		 self.assertFalse(form.is_valid())
	
	def test_UserPreferencesForm_Missing_Ethnicity(self):
		 form = EditPartnerPrefrencesForm(data={"location":"35 boronia road boronia","sex":"male","age":"24","ethnicity":""})
		 self.assertFalse(form.is_valid())
		 
		 
class FoodPreferencesForm_Test(TestCase):