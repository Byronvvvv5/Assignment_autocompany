from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase,APIClient


client = APIClient()
client.defaults['HTTP_HOST'] = 'http://127.0.0.1:8000/'
client.defaults['HTTP_CONTENT_TYPE'] = 'application/json'

class AuthenticationTests(APITestCase):

    urls = {
        'signup': reverse("token_auth-signup"),
        'login': reverse("token_auth-login")
    }

    users = {
        'admin': {
            'credentials': {"username": "admin", "password": "admin1234"}
        },
        'client': {
            'credentials': {"username": "client", "password": "client"}
        },
    }

    def test_user_signup_correctly(self):
        credentials = self.users['client']['credentials']
        url = self.urls['signup']
        response = self.client.post(url, credentials, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], credentials["username"])


    def test_user_cannot_signup_with_no_data(self):
        url = self.urls['signup']
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_login_with_good_credentials(self):
        credentials = self.users['admin']['credentials']
        url = self.urls['login']
        response = self.client.post(url, credentials, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in response.data)


    def test_login_with_bad_credentials(self):
        credentials = self.users['admin']['credentials'].copy()
        credentials['password'] = "badPassword"
        url = self.urls['login']
        response = self.client.post(url, credentials, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
