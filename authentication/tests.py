from django.test import TestCase

# Create your tests here.

import unittest
from unittest.mock import patch

from .views import GoogleLogin

class TestAuthGoogle(unittest.TestCase):

    @patch('auth.requests.post') 
    def test_auth_google_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'access_token': 'abc123'}
        
        response = GoogleLogin({'code': '123'})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['access_token'], 'abc123')

    def test_auth_google_invalid_code(self):
        response = GoogleLogin({'code': None})
        
        self.assertEqual(response.status_code, 400)

    def test_auth_google_error(self):
        mock_post.return_value.status_code = 500
        
        response = GoogleLogin({'code': '123'})
        
        self.assertEqual(response.status_code, 500)

