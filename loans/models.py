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
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2,)
    status = models.CharField(max_length=1, default=LoanState.New)
    emi = models.DecimalField(max_digits=5, decimal_places=0, default=0)

    def save(self, *args, **kwargs):
        self.emi = self.calculate_emi()
        return super().save(*args, **kwargs)

    def calculate_emi(self):
        """ Individuals can calculate personal loan EMI by using the following formula -
            E = P * r * (1+r) ^n / ((1+r) ^n-1)
            Here,
                E denotes the EMI amount.
                P gives the principal or loan amount applied for.
                r is the applicable rate of interest, calculate on a per month basis.
                n denotes loan tenure.

            references:
                https://emicalculator.net/
                https://www.icicibank.com/calculator/personal-loan-emi-calculator.page
        """
        P = self.requested_principal
        r = self.interest_rate / (12 * 100)  # interest rate per month
        n = self.duration_in_months
        print(P, r, n)
        return P * r * (((1 + r) ** n) / (((1 + r) ** n) - 1))

    def mark_approved(self):
        self.status = LoanState.Approved
        self.save()
        return self

    def mark_rejected(self):
        self.status = LoanState.Rejected
        self.save()
        return self

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
