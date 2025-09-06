from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer
from services.mpesa import MpesaService   # lowercase services, not Services

class DepositView(APIView):
    def post(self, request):
        # Deposit logic
        return Response({"message": "Deposit successful"}, status=status.HTTP_201_CREATED)

class WithdrawView(APIView):   # 👈 must be here!
    def post(self, request):
        # Withdrawal logic
        return Response({"message": "Withdrawal successful"}, status=status.HTTP_201_CREATED)

class TransactionListView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
