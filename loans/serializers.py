from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Loan
User = get_user_model()


class LoanSerializer(serializers.ModelSerializer):
    beneficiary = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True
    )

    class Meta:
        model = Loan
        read_only_fields = ["status", "agent", "admin", "emi"]

        fields = [
            "id",
            "beneficiary",
            "requested_principal",
            "interest_rate",
            "duration_in_months",
        ] + read_only_fields
