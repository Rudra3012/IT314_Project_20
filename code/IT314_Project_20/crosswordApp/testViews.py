from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.test import TestCase, Client

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('login')
        self.sign = reverse('signup')
        self.homee = reverse('home')
        self.fp = reverse('forget_password')

    def test_login_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')

    def test_signUp_GET(self):
        response = self.client.get(self.sign)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_home_GET(self):
        response = self.client.get(self.homee)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_forgot_password_GET(self):
        response = self.client.get(self.fp)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'forget_password.html')