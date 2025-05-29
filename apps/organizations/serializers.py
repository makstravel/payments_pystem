from rest_framework import serializers

class BalanceSerializer(serializers.Serializer):
    inn = serializers.CharField()
    balance = serializers.IntegerField()
