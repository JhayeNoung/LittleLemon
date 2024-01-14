from django.contrib.auth.models import User
from django.test import TestCase

class UserTest(TestCase):
    def setUp(self):
        User.objects.create_user(id=1, username='james')

    def testing(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'james')