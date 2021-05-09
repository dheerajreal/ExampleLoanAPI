from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from loans.models import Loan

# Create your tests here.


class LoanObjectTests(TestCase):
    def setUp(self):
        self.usermodel = get_user_model()
        self.demoadmin = self.usermodel.objects.create_user(
            username="demoadmin",
            password='password',
            is_admin=True
        )
        self.demoagent = self.usermodel.objects.create_user(
            username="demoagent",
            password='password',
            is_agent=True
        )
        self.demobeneficiary = self.usermodel.objects.create_user(
            username="demobeneficiary",
            password='password',
        )
        self.demoloan = Loan.objects.create(
            duration_in_months=72,
            requested_principal=50000,
            interest_rate=10.5,
            beneficiary=self.demobeneficiary,
            agent=self.demoagent
        )

    def test_loan_create(self):
        self.assertEqual(939, round(self.demoloan.calculate_emi()))
        self.assertEqual(self.demoloan.emi, self.demoloan.calculate_emi())
        self.assertEqual(self.demoloan.status, "N")
        self.assertEqual(self.demoloan.agent, self.demoagent)
        self.assertEqual(self.demoloan.beneficiary, self.demobeneficiary)

    def test_loan_approve(self):
        self.assertTrue(self.demoloan.is_editable)
        self.demoloan.mark_approved()
        self.assertFalse(self.demoloan.is_editable)
        self.assertEqual(self.demoloan.status, "A")

    def test_loan_reject(self):
        self.assertTrue(self.demoloan.is_editable)
        self.demoloan.mark_rejected()
        self.assertTrue(self.demoloan.is_editable)
        self.assertEqual(self.demoloan.status, "R")

    def test_loan_create_api_endpoint_access(self):
        response = self.client.get(reverse("loan_create"))
        self.assertEqual(response.status_code, 403)  # before login
        self.client.login(username="demoadmin", password="password")
        response = self.client.get(reverse("loan_create"))
        self.assertEqual(response.status_code, 200)  # after login
