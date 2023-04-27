import json
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.test import TestCase, Client

from crosswordApp.views import LoginPage, SignupPage, create_crossword, crossword_list_view, create_crossword_automatic, create_crossword_manual, creation, home, CreatorProfile, adminPage, AdminUserListPage, AdminCrosswordListPage, AdminModifyCrosswordPage, ProcessModifyUserRequest, forget_password, ChangePassword, puzzle_of_day, solve_crossword


class TestUrls(SimpleTestCase):

    def test_list_url_resolves1(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, LoginPage)

    def test_list_url_resolves2(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, SignupPage)

    def test_list_url_resolves3(self):
        url = reverse('create_crossword')
        self.assertEquals(resolve(url).func, create_crossword)

    def test_list_url_resolves4(self):
        url = reverse('crossword_list_view')
        self.assertEquals(resolve(url).func, crossword_list_view)

    def test_list_url_resolves5(self):
        url = reverse('create_crossword_automatic')
        self.assertEquals(resolve(url).func, create_crossword_automatic)

    def test_list_url_resolves6(self):
        url = reverse('creation')
        self.assertEquals(resolve(url).func, creation)

    def test_list_url_resolves7(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)


    def test_list_url_resolves8(self):
        url = reverse('adminPage')
        self.assertEquals(resolve(url).func, adminPage)

    def test_list_url_resolves9(self):
        url = reverse('AdminCrosswordListPage')
        self.assertEquals(resolve(url).func, AdminCrosswordListPage)

    def test_list_url_resolves10(self):
        url = reverse('AdminUserListPage')
        self.assertEquals(resolve(url).func, AdminUserListPage)



    def test_list_url_resolves12(self):
        url = reverse('forget_password')
        self.assertEquals(resolve(url).func, forget_password)



    def test_list_url_resolves14(self):
        url = reverse('puzzle_of_day')
        self.assertEquals(resolve(url).func, puzzle_of_day)



    def test_list_url_resolves16(self):
        url = reverse('create_crossword_manual')
        self.assertEquals(resolve(url).func, create_crossword_manual)





class TestViews(TestCase):

    def setUp(self):
        self.client=Client()
        self.list_url=reverse('login')

    def test_login_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')

# class TestAuth(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_login1(self):
#         response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'ruchir123'})
#         r = json.loads(response.content)
#         self.assertEqual(r['message'], 'Login Unsuccessful')
#
#     # password is not valid. No use of Capital letter and special character.
#
#     def test_login2(self):
#         response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'Ruchir123'})
#         r = json.loads(response.content)
#         self.assertEqual(r['message'], 'Login Unsuccessful')
#
#     # password is not valid. No special character.
#
#     def test_login3(self):
#         response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'Ru@123'})
#         r = json.loads(response.content)
#         self.assertEqual(r['message'], 'Login Unsuccessful')
#
#     # password is not valid. Number of characters should be more than 8.
#
#     def test_login4(self):
#         response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'Ru@123'})
#         r = json.loads(response.content)
#         self.assertEqual(r['message'], 'Login Unsuccessful')
#
#     # password is not valid. Number of characters should be less than 24.
#
#     def test_login5(self):
#         response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'Ruchir@123'})
#         r = json.loads(response.content)
#         self.assertEqual(r['message'], 'Login Successful')
#
#     # Account logged in  Successfully.
#
#     def test_login6(self):
#         response = self.client.post('/login/', {'username': 'Ruchir17', 'pass': 'Rdarjir@123'})
#         r = json.loads(response.content)
#         self.assertEqual(r['message'], 'Login Successful')
#
#     # Account logged in  Successfully.
#
#     def test_login7(self):
#         response = self.client.post('/login/', {'username': 'Jainam 21', 'pass': 'Jadu@2108'})
#         r = json.loads(response.content)
#         self.assertEqual(r['message'], 'Login Unsuccessful')
#
#     # User Name is not valid as it contains space.
#
#     def test_login8(self):
#         response = self.client.post('/login/', {'username': 'Jainam-21', 'pass': 'Jadu@2108'})
#         r = json.loads(response.content)
#         self.assertEqual(r['message'], 'Login Successful')
#
#     # User Name can contain '-'. Account Logged in Successfully.
#
#     def test_login9(self):
#         response = self.client.post('/login/', {'username': 'Jainam_21', 'pass': 'Jadu@2108'})
#         r = json.loads(response.content)
#         self.assertEqual(r['message'], 'Login Successful')
#
#     # User Name can contain '_'. Account Logged in Successfully
#
#     def test_login10(self):
#         response = self.client.post('/login/', {'username': 'Dev', 'pass': 'DevD@0307'})
#         r = json.loads(response.content)
#         self.assertEqual(r['message'], 'Login Unsuccessful')
#
#     #  User name is not valid. Number of characters should be more than 4.
#
#     def test_login11(self):
#         response = self.client.post('/login/', {'username': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'pass': 'DevD@0307'})
#         r = json.loads(response.content)
#         self.assertEqual(r['message'], 'Login Unsuccessful')
#
#     # User Name is not valid. Number of characters should be less than 15.
#