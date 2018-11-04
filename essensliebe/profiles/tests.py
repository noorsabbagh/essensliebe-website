from django.test import TestCase
from django.contrib.auth.models import User

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
