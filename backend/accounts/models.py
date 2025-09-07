from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TX_TYPE = (("deposit", "Deposit"), ("withdrawal", "Withdrawal"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tx_type = models.CharField(max_length=20, choices=TX_TYPE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default="pending")
    reference = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.tx_type} - {self.amount}"
