from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.permissions import (AdminPermission, AgentPermission,
                                  ExclusivelyAgentPermission)

from .models import Loan
from .serializers import LoanSerializer


class MyLoansListView(generics.ListAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Loan.get_all_loans().filter(beneficiary=self.request.user)


class AllLoansListView(generics.ListAPIView):
    queryset = Loan.get_all_loans()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]


class RejectedLoansListView(generics.ListAPIView):
    queryset = Loan.get_rejected_loans()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]


class ApprovedLoansListView(generics.ListAPIView):
    queryset = Loan.get_approved_loans()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]


class NewRequestedLoansListView(generics.ListAPIView):
    queryset = Loan.get_new_requested_loans()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]


class LoanCreateView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = [
        "status",
        "beneficiary",
        "agent",
        "admin",
    ]
    ordering_fields = [
        "requested_datetime",
        "edited_datetime",
        "requested_principal",
        "emi"
    ]
    ordering = ["pk"]

    def perform_create(self, serializer):
        serializer.save(agent=self.request.user)


class LoanUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Loan.get_non_approved_loans()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, ExclusivelyAgentPermission]


@api_view(['POST'])
@permission_classes([IsAuthenticated, AdminPermission])
def loan_approve_view(request, pk):
    loan_object = get_object_or_404(Loan.get_non_approved_loans(), pk=pk)
    loan_object.admin = request.user
    loan_object = loan_object.mark_approved()
    return Response(LoanSerializer(loan_object).data)
