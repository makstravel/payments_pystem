from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Organization
from .serializers import BalanceSerializer
from django.shortcuts import get_object_or_404

class OrganizationBalanceAPIView(APIView):
    """
    Возвращает баланс организации по ИНН.
    """
    def get(self, request, inn):
        org = get_object_or_404(Organization, inn=inn)
        serializer = BalanceSerializer({"inn": org.inn, "balance": org.balance})
        return Response(serializer.data)
