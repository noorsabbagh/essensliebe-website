from django.test import TestCase
from django.contrib.auth.models import User
from .forms import *

class Setup_Class(TestCase):
	
	def setUp(self):
		self.user = User.objects.create(username="testyMcTesty",password="TestymcTest1",first_name="test",last_name="mcTest",email="test@test.me")
		
class UserRegistrationForm_Test(TestCase):
	
	def test_UserRegistrationForm_valid(self):
		 form = UserRegistrationForm(data={"username":"testymctest","email": "test@test.me","email2": "test@test.me", "password": "TestymcTest1", "first_name": "test", "last_name": "test"})
		 self.assertTrue(form.is_valid())
		 
	def test_UserRegistrationForm_Missing_username(self):
		form = UserRegistrationForm(data={"username":"","email": "test@test.me","email2": "test@test.me", "password": "TestymcTest1", "first_name": "test", "last_name": "test"})
		self.assertFalse(form.is_valid())
	
	def test_UserRegistrationForm_Missing_email(self):
		form = UserRegistrationForm(data={"username":"testymctest","email": "","email2": "test@test.me", "password": "TestymcTest1", "first_name": "test", "last_name": "test"})
		self.assertFalse(form.is_valid())
	
	def test_UserRegistrationForm_Missing_email2(self):
		form = UserRegistrationForm(data={"username":"testymctest","email": "test@test.me","email2": "", "password": "TestymcTest1", "first_name": "test", "last_name": "test"})
		self.assertFalse(form.is_valid())
	
	def test_UserRegistrationForm_Missing_password(self):
		 form = UserRegistrationForm(data={"username":"testymctest","email": "test@test.me","email2": "test@test.me", "password": "", "first_name": "test", "last_name": "test"})
		 self.assertFalse(form.is_valid())
		 
	def test_UserRegistrationForm_Missing_password(self):
		 form = UserRegistrationForm(data={"username":"testymctest","email": "test@test.me","email2": "test@test.me", "password": "", "first_name": "test", "last_name": "test"})
		 self.assertFalse(form.is_valid())
		 
	def test_UserRegistrationForm_Missing_firstName(self):
		 form = UserRegistrationForm(data={"username":"testymctest","email": "test@test.me","email2": "test@test.me", "password": "TestymcTest1", "first_name": "", "last_name": "test"})
		 self.assertFalse(form.is_valid())

	def test_UserRegistrationForm_Missing_lastName(self):
		 form = UserRegistrationForm(data={"username":"testymctest","email": "test@test.me","email2": "test@test.me", "password": "TestymcTest1", "first_name": "test", "last_name": ""})
		 self.assertFalse(form.is_valid())
		 
	def test_UserRegistrationForm_Invaild_password(self):
		 form = UserRegistrationForm(data={"username":"testymctest","email": "test@test.me","email2": "test@test.me", "password": "hi", "first_name": "test", "last_name": "test"})
		 self.assertFalse(form.is_valid())
		 
	def test_UserRegistrationForm_Invaild_Username(self):
		 form = UserRegistrationForm(data={"username":"$$#%!@$^User11123","email": "test@test.me","email2": "test@test.me", "password": "Hi45446652", "first_name": "test", "last_name": "test"})
		 self.assertFalse(form.is_valid())
