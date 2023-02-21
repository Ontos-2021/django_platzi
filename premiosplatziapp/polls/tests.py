import datetime

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

from .models import Question

class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_questions(self):
        '''was_published_recently returns False for questions whose pub_date is in the future'''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text = "¿Quién es el mejor Course Director de Platzi?", pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)

class QuestionIndexViewTest(TestCase):

    def test_no_questions(self):
        """If no question exists, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.content["latest_question_list"], [])

    def test_no_future_questions_are_displayed(self):
        '''If a future question is created in the database, this question isn't shown until 
        his pub_date is equal to the present time'''
        response = self.client.get(reverse("polls:index"))
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Who is the best Student?", pub_date=time)
        self.assertNotIn(future_question, response.context["latest_question_list"])
        