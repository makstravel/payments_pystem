from rest_framework import serializers

class BankWebhookSerializer(serializers.Serializer):
    operation_id = serializers.UUIDField()
    amount = serializers.IntegerField(min_value=1)
    payer_inn = serializers.CharField(max_length=12)
    document_number = serializers.CharField(max_length=32)
    document_date = serializers.DateTimeField()
