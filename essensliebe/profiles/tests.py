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
	
class UserPrefDB_Test(TestCase):

	def setUp(self):
		self.user = User.objects.create_user(username="memehunter76",password="TestymcTest1",first_name="test",last_name="mcTest",email="memehunter76@test.me")
		self.login = self.client.login(username=self.user.username, password="TestymcTest1")
	
	def test_UserPrefDB_(self):
		data={"location":"35 boronia road boronia","sex":"male","age":"24","ethnicity":"white"}
		profile = "/profile/" + self.user.username + "/edit/"
		response = self.client.post(profile,data,follow=True)
		self.assertTrue(response.request["PATH_INFO"])
		
class UserPref_Food_DB_Test(TestCase):

	def setUp(self):
		self.user = User.objects.create_user(username="memehunter76",password="TestymcTest1",first_name="test",last_name="mcTest",email="memehunter76@test.me")
		self.login = self.client.login(username=self.user.username, password="TestymcTest1")
	
	def test_UserPref_Food_DB_(self):
		data={"fav_food":"bread","vegan":"yes","vegetarian":"yes"}
		profile = "/profile/" + self.user.username + "/edit/"
		response = self.client.post(profile,data,follow=True)
		self.assertTrue(response.request["PATH_INFO"])
		 
		 
class FoodPreferencesForm_Test(TestCase):
	
	def test_FoodPreferencesForm_Valid(self):
		 form = EditFoodPrefrencesForm(data={"fav_food":"bread","vegan":"yes","vegetarian":"yes"})
		 self.assertFalse(form.is_valid())
		 
	def test_UserPreferencesForm_Invalid_FavFood(self):
		 form = EditFoodPrefrencesForm(data={"fav_food":"bread2323","vegan":"yes","vegetarian":"yes"})
		 self.assertFalse(form.is_valid())
		 
	def test_UserPreferencesForm_Invalid_vegan(self):
		 form = EditFoodPrefrencesForm(data={"fav_food":"bread","vegan":"SELECT USER23","vegetarian":"yes"})
		 self.assertFalse(form.is_valid())
		
	def test_UserPreferencesForm_Invalid_vegatarian(self):
		 form = EditFoodPrefrencesForm(data={"fav_food":"bread","vegan":"yes","vegetarian":"SELECT USER23"})
		 self.assertFalse(form.is_valid())
		 
	def test_UserPreferencesForm_Missing_FavFood(self):
		 form = EditFoodPrefrencesForm(data={"fav_food":"","vegan":"yes","vegetarian":"yes"})
		 self.assertFalse(form.is_valid())
		 
	def test_UserPreferencesForm_Missing_vegan(self):
		 form = EditFoodPrefrencesForm(data={"fav_food":"bread","vegan":"","vegetarian":"yes"})
		 self.assertFalse(form.is_valid())
		
	def test_UserPreferencesForm_Missing_vegatarian(self):
		 form = EditFoodPrefrencesForm(data={"fav_food":"bread","vegan":"yes","vegetarian":""})
		 self.assertFalse(form.is_valid())
		 
		 
