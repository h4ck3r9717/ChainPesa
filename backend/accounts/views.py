from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # 👈 Add this
from .models import Transaction
from .serializers import TransactionSerializer
from services.mpesa import MpesaService   # lowercase services, not Services


class DepositView(APIView):
    permission_classes = [IsAuthenticated]  # 👈 protect endpoint

    def post(self, request):
        # Example: connect with Mpesa service (you can expand later)
        # MpesaService().deposit(request.user, request.data)
        return Response({"message": "Deposit successful"}, status=status.HTTP_201_CREATED)


class WithdrawView(APIView):
    permission_classes = [IsAuthenticated]  # 👈 protect endpoint

    def post(self, request):
        # Example: MpesaService().withdraw(request.user, request.data)
        return Response({"message": "Withdrawal successful"}, status=status.HTTP_201_CREATED)


class TransactionListView(APIView):
    permission_classes = [IsAuthenticated]  # 👈 protect endpoint

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)  # 👈 only user’s transactions
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
