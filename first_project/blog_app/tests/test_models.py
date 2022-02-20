from django.http import HttpRequest
from django.test import TestCase, Client
from django.urls import reverse
import unittest
from blog_app.views import *
from blog_app.models import *
from model_mommy import mommy


class viewstesting(TestCase):
    def test_view_not_owner(self):
        response = self.client.get('url/topics/9')
        self.assertEqual(response.status_code, 404)


    def test_view_owner(self):
        self.client.force_login('dmvrb', password='123456')
        response = self.client.get('url/topics/9')
        self.assertEqual(response.status_code, 200)