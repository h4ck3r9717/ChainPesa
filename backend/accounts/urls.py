from django.urls import path
from .views import DepositView, WithdrawView, TransactionListView

urlpatterns = [
    path("deposit/", DepositView.as_view(), name="deposit"),
    path("withdraw/", WithdrawView.as_view(), name="withdraw"),
    path("transactions/", TransactionListView.as_view(), name="transactions"),
]
