from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class LoanState:
    New = "N"
    Approved = "A"
    Rejected = "R"


class Loan(models.Model):
    beneficiary = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="beneficiary"
    )
    agent = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="agent"
    )
    admin = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="admin"
    )
    duration_in_months = models.PositiveSmallIntegerField(blank=True,
                                                          null=True,)
    requested_principal = models.DecimalField(max_digits=5, decimal_places=0,)
    interest_rate = models.FloatField(max_length=3)
    status = models.CharField(max_length=1, default=LoanState.New)
    emi = models.DecimalField(max_digits=5, decimal_places=0, default=0)

