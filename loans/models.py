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

    def mark_approved(self):
        self.status = LoanState.Approved
        self.save()

    def mark_rejected(self):
        self.status = LoanState.Rejected
        self.save()

    @property
    def is_editable(self):
        return self.status != LoanState.Approved

    @classmethod
    def get_all_loans(cls):
        return cls.objects.all()

    @classmethod
    def get_rejected_loans(cls):
        return cls.objects.filter(status=LoanState.Rejected)

    @classmethod
    def get_approved_loans(cls):
        return cls.objects.filter(status=LoanState.Approved)

    @classmethod
    def get_new_requested_loans(cls):
        return cls.objects.filter(status=LoanState.New)

    @classmethod
    def get_non_approved_loans(cls):
        return cls.objects.exclude(status=LoanState.Approved)
