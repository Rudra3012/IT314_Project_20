import json

from django.test import TestCase, Client


class TestAuth(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login1(self):
        response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'ruchir123'})
        r = json.loads(response.content)
        self.assertEqual(r['message'], 'Login Unsuccessful')

    # password is not valid. No use of Capital letter and special character.

    def test_login2(self):
        response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'Ruchir123'})
        r = json.loads(response.content)
        self.assertEqual(r['message'], 'Login Unsuccessful')

    # password is not valid. No special character.

    def test_login3(self):
        response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'Ru@123'})
        r = json.loads(response.content)
        self.assertEqual(r['message'], 'Login Unsuccessful')

    # password is not valid. Number of characters should be more than 8.

    def test_login4(self):
        response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'Ru@123'})
        r = json.loads(response.content)
        self.assertEqual(r['message'], 'Login Unsuccessful')

    # password is not valid. Number of characters should be less than 24.

    def test_login5(self):
        response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'Ruchir@123'})
        r = json.loads(response.content)
        self.assertEqual(r['message'], 'Login Successful')

    # Account logged in  Successfully.

    def test_login6(self):
        response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'Rdarjir@123'})
        r = json.loads(response.content)
        self.assertEqual(r['message'], 'Login Successful')

    # Account logged in  Successfully.

    def test_login7(self):
        response = self.client.post('/login/', {'username': 'Jainam 21', 'pass': 'Jadu@2108'})
        r = json.loads(response.content)
        self.assertEqual(r['message'], 'Login Unsuccessful')

    # User Name is not valid as it contains space.

    def test_login8(self):
        response = self.client.post('/login/', {'username': 'Jainam-21', 'pass': 'Jadu@2108'})
        r = json.loads(response.content)
        self.assertEqual(r['message'], 'Login Successful')

    # User Name can contain '-'. Account Logged in Successfully.

    def test_login9(self):
        response = self.client.post('/login/', {'username': 'Jainam_21', 'pass': 'Jadu@2108'})
        r = json.loads(response.content)
        self.assertEqual(r['message'], 'Login Successful')

    # User Name can contain '_'. Account Logged in Successfully

    def test_login10(self):
        response = self.client.post('/login/', {'username': 'Dev', 'pass': 'DevD@0307'})
        r = json.loads(response.content)
        self.assertEqual(r['message'], 'Login Unsuccessful')

    #  User name is not valid. Number of characters should be more than 4.

    def test_login11(self):
        response = self.client.post('/login/', {'username': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'pass': 'DevD@0307'})
        r = json.loads(response.content)
        self.assertEqual(r['message'], 'Login Unsuccessful')

    # User Name is not valid. Number of characters should be less than 15.


