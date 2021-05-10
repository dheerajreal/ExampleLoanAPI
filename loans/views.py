from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from accounts.permissions import (AdminPermission, AgentPermission,
                                  ExclusivelyAgentPermission)

from .models import Loan
from .serializers import LoanSerializer


class MyLoansListView(generics.ListAPIView):
    """Loans for a specific beneficiary user"""
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Loan.get_all_loans().filter(beneficiary=self.request.user)
        else:
            return None


class AllLoansListView(generics.ListAPIView):
    """All loans,
    can be used only by admins, agents and staff"""
    queryset = Loan.get_all_loans()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]


class RejectedLoansListView(generics.ListAPIView):
    """Rejected loans,
    can be used only by admins, agents and staff"""
    queryset = Loan.get_rejected_loans()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]


class ApprovedLoansListView(generics.ListAPIView):
    """Approved loans,
    can be used only by admins, agents and staff"""
    queryset = Loan.get_approved_loans()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]


class NewRequestedLoansListView(generics.ListAPIView):
    """Loan requests that have't been accepted or rejected yet,
    can be used only by admins, agents and staff"""
    queryset = Loan.get_new_requested_loans()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]


class LoanCreateView(generics.ListCreateAPIView):
    """Create new Loan requests,
    See loans with filtering and ordering options,
    can be used only by admins, agents and staff"""
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
    """Update a specific loan,
    can be used only by agents"""
    queryset = Loan.get_non_approved_loans()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, ExclusivelyAgentPermission]


@api_view(['POST'])
@permission_classes([IsAuthenticated, AdminPermission])
def loan_approve_view(request, pk):
    """Approve loans, Admin or staff only"""
    loan_object = get_object_or_404(Loan, pk=pk)
    if not loan_object.is_editable:
        raise PermissionDenied("already approved")
    loan_object.admin = request.user
    loan_object = loan_object.mark_approved()
    return Response(LoanSerializer(loan_object).data)
