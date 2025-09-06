from services.mpesa import MpesaService
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
import uuid


class DepositView(APIView):
    def post(self, request):
        amount = request.data.get("amount")
        phone = request.data.get("phone")  # user’s phone number for M-Pesa
        if not amount or not phone:
            return Response({"error": "Amount and phone are required"}, status=400)

        mpesa = MpesaService()
        result = mpesa.stk_push(phone, amount)

        tx = Transaction.objects.create(
            user=request.user,
            tx_type="deposit",
            amount=amount,
            status="pending",
            reference=result.get("CheckoutRequestID", "mpesa-"+str(uuid.uuid4()))
        )

        return Response({"transaction": TransactionSerializer(tx).data, "mpesa_response": result}, status=201)
