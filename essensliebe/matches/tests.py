from django.test import TestCase

from django.test import TestCase
from django.contrib.auth.models import User
from questions.models import Question


class matchingTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='memeHunter72', password='memeHunter72', first_name='Meme', last_name='Oof', email='oof@meme.com')
        self.user2 = User.objects.create_user(username='memeHunter722', password='memeHunter722', first_name='Meme', last_name='Oof', email='oof2@meme.com')
        self.login = self.client.login(username=self.user.username, password='memeHunter72')

    def test_Match_No_Questions(self):
        response = self.client.post("/matches/", follow=True)
        self.assertTrue(response.context["matches"] == [])

    def test_Match_After_60_Questions(self):
        self.login = self.client.login(username=self.user.username, password='memeHunter72')
        self.__questions()
        self.client.logout()
        self.login2 = self.client.login(username=self.user2.username, password='memeHunter722')
        self.__questions()
        response1 = self.client.post("/matches/", follow=True)
        self.assertTrue(response1.context["matches"] != [])

    def __questions(self):
        for i in range(30):
             data = {"question_id": i,
                  "answer_id": i,
                  "importance_level": "Mandatory",
                  "their_answer_id": -1,
                  "their_importance_level": "Mandatory"}
             response = self.client.post("/questions/"+str(i), data)