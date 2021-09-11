from apps.accounts.models import User
from django.test import TestCase


class UserModelTests(TestCase):
    def test_str_method(self):
        user = User(username='ali')
        self.assertEqual(str, type(user.get_full_name()))
        self.assertEqual(user.get_full_name(), user.username)
        user.first_name = 'Ali'
        user.last_name = 'Big'
        self.assertEqual('Ali Big', user.get_full_name())
