from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):
    def setUp(self):
        self.usermodel = get_user_model()

    def test_create_user(self):
        user = self.usermodel.objects.create_user(
            username="user",
            email='person@example.com',
            password='password'
        )
        self.assertEqual(user.email, 'person@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = self.usermodel.objects.create_superuser(
            username="adminuser",
            email='admin@example.com',
            password='password'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
