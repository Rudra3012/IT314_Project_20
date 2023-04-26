from django.test import SimpleTestCase
from django.urls import reverse, resolve

from crosswordApp.views import LoginPage


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, LoginPage)
