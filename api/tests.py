from django.test import TestCase
from django.urls import reverse


class HelloAPITests(TestCase):

    def test_hello_api_returns_200(self):
        response = self.client.get(reverse('hello_api'))
        self.assertEqual(response.status_code, 200)

    def test_hello_api_returns_correct_message(self):
        response = self.client.get(reverse('hello_api'))
        self.assertEqual(
            response.json()['message'],
            "Hello from CSC 325 CI/CD Pipeline!"
        )

    
    def test_hello_api_returns_success_status(self):
        response = self.client.get(reverse('hello_api'))
        self.assertEqual(
            response.json()['status'],
            "success"
        )

    
    def test_hello_api_returns_success_status(self):
        response = self.client.get(reverse('hello_api'))
        self.assertEqual(
            response.json()['status'],
            "success"
        )
