from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BankWebhookSerializer
from .services import process_bank_webhook

class BankWebhookAPIView(APIView):
    """
    Обработка входящих webhook-ов банка.
    """

    def post(self, request):
        serializer = BankWebhookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = process_bank_webhook(serializer.validated_data)

        # В любом случае возвращаем 200 OK, но поведение разное:
        if not result:
            # Логируем, что дубль не обработан
            return Response({"detail": "Дублирующая операция, баланс не изменён."}, status=status.HTTP_200_OK)

        return Response({"detail": "Платёж успешно проведён."}, status=status.HTTP_200_OK)
