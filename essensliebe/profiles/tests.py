from django.test import TestCase
from .models import PartnerPrefrences, FoodPrefrences
from .forms import *

class Setup_Class(TestCase):
	
	def setUp(self):
		self.user = User.objects.create(username="testyMcTesty" ,password="pass1234")

		
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