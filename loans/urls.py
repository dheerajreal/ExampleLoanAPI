from django.urls import path

from .views import LoanCreateView, LoanUpdateView, loan_approve_view

urlpatterns = [
    path('', LoanCreateView.as_view(), name="loan_create"),
    path('<int:pk>/edit/', LoanUpdateView.as_view(), name="loan_update"),
    path('<int:pk>/approve/', loan_approve_view, name="loan_approve"),



]
