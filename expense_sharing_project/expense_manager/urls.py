from django.urls import path
from .views import BalanceListCreateView, MyHTMLView
from .views import ExpenseCreateView

urlpatterns = [
    # Existing URL patterns
    path('balances/', BalanceListCreateView.as_view(), name='balance-list-create'),
    path('expenses/', MyHTMLView.as_view(), name='expense-list'),
    path('create_expense/', ExpenseCreateView.as_view(), name='create-expense'),
]
