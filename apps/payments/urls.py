from django.urls import path
from .views import BankWebhookAPIView

urlpatterns = [
    path('webhook/bank/', BankWebhookAPIView.as_view(), name='bank-webhook'),
]
