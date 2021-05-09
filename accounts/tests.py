from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class UsersManagersTests(TestCase):
    def setUp(self):
        self.usermodel = get_user_model()
        self.demouser = self.usermodel.objects.create_user(
            username="demouser",
            password='password',
            is_admin=True
        )

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
        self.assertFalse(user.is_agent)
        self.assertFalse(user.is_admin)

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
        self.assertFalse(admin_user.is_agent)
        self.assertFalse(admin_user.is_admin)

    def test_api_endpoint_access(self):
        response = self.client.get(reverse("user_list_create"))
        self.assertEqual(response.status_code, 403)  # before login
        self.client.login(username="demouser", password="password")
        response = self.client.get(reverse("user_list_create"))
        self.assertEqual(response.status_code, 200)  # after login
