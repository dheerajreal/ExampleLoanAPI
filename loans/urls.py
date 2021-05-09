from django.urls import path

from .views import (AllLoansListView, ApprovedLoansListView, LoanCreateView,
                    LoanUpdateView, MyLoansListView, NewRequestedLoansListView,
                    RejectedLoansListView, loan_approve_view)

urlpatterns = [
    path('', LoanCreateView.as_view(), name="loan_create"),
    path('<int:pk>/edit/', LoanUpdateView.as_view(), name="loan_update"),
    path('<int:pk>/approve/', loan_approve_view, name="loan_approve"),

    path('list/all/', AllLoansListView.as_view(), name="list_loan_all"),
    path('list/new/', NewRequestedLoansListView.as_view(), name="list_loan_new"),
    path('list/rejected/', RejectedLoansListView.as_view(),
         name="list_loan_rejected"),
    path('list/approved/', ApprovedLoansListView.as_view(),
         name="list_loan_approved"),
    path('list/mine/', MyLoansListView.as_view(), name="list_loan_mine"),


]
