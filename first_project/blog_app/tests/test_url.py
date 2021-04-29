from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from .. import views, urls


class PageTests(SimpleTestCase):

    def test_home_page(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/index.html')


    def test_home_page_does_not_contain(self):
        response = self.client.get('')
        self.assertNotContains(
            response, 'Text that shouldnt be showed.')

    def test_topic_page(self):
        response = self.client.get('/topics/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/topics.html')
