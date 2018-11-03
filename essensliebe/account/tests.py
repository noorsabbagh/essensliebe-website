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
		 
	def test_UserRegistrationForm_Invalid_password(self):
		 form = UserRegistrationForm(data={"username":"testymctest","email": "test@test.me","email2": "test@test.me", "password": "hi", "first_name": "test", "last_name": "test"})
		 self.assertFalse(form.is_valid())
		 
	def test_UserRegistrationForm_Invalid_Username(self):
		 form = UserRegistrationForm(data={"username":"$$#%!@$^User11123","email": "test@test.me","email2": "test@test.me", "password": "Hi45446652", "first_name": "test", "last_name": "test"})
		 self.assertFalse(form.is_valid())
		
	def test_UserRegistrationForm_Emails_DNTMatch(self):
		 form = UserRegistrationForm(data={"username":"testymctest","email": "test@test.me2","email2": "test@test.me", "password": "TestymcTest1", "first_name": "test", "last_name": "test"})
		 self.assertFalse(form.is_valid())
		 
	def test_UserRegistrationForm_Invalid_Email(self):
		 form = UserRegistrationForm(data={"username":"testymctest","email": "testtest.me","email2": "testtest.me", "password": "TestymcTest1", "first_name": "test", "last_name": "test"})
		 self.assertFalse(form.is_valid())

class UserLoginForm_Test(TestCase):

	def test_UserLoginForm_Valid(self):
		 form = UserLoginForm(data={"username":"testymctest", "password": "TestymcTest1"})
		 self.assertFalse(form.is_valid())

		 
	def test_UserLoginForm_Invalid(self):
		 form = UserLoginForm(data={"username":"$$#%!@$^User11123", "password": "Hi45446652"})
		 self.assertFalse(form.is_valid())
		 
	def test_UserLoginForm_Invalid_Username(self):
		form = UserLoginForm(data={"username":"$$#%!@$^User11123", "password": "TestymcTest1"})
		self.assertFalse(form.is_valid())
		
	def test_UserLogin_Form_Invalid_Password(self):
		form = UserLoginForm(data={"username":"testymctest", "password": "Hi45446652"})
		self.assertFalse(form.is_valid())
		
	def test_UserLogin_Form_Missing_Password(self):
		form = UserLoginForm(data={"username":"testymctest", "password": ""})
		self.assertFalse(form.is_valid())
		
	def test_UserLoginForm_Missing_Username(self):
		form = UserLoginForm(data={"username":"", "password": "TestymcTest1"})
		self.assertFalse(form.is_valid())