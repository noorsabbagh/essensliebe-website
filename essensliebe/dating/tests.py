from django.test import TestCase 
from django.contrib.auth.models import User 
 
class datingTests(TestCase): 
 
    def setUp(self): 
        self.user = User.objects.create_user(username='memeHunter72', password='memeHunter72', first_name='Meme', last_name='Oof', email='oof@meme.com') 
        self.login = self.client.login(username=self.user.username, password='memeHunter72') 
 
    def test_Dating_No_Address(self): 
        response = self.client.post("/dating/", follow=True) 
        self.assertTrue(response.status_code == 218) 
 
    def test_Dating_No_Address(self): 
        data = {"location": "13 Random St Frankston", 
                "sex": "male", 
                "age": "19", 
                "ethnicity": "White", 
                "description": "Hi", 
                "picture": None 
                 } 
        profile = "/profile/" + self.user.username + "/edit/" 
        response = self.client.post(profile, data, follow=True) 
        response = self.client.post("/dating/", follow=True) 
        self.assertTrue(response.status_code == 200) 

