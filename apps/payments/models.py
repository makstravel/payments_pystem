from django.db import models

class Payment(models.Model):
    """Модель платежа от банка."""
    operation_id = models.UUIDField("ID операции", unique=True, db_index=True)
    amount = models.BigIntegerField("Сумма")
    payer_inn = models.CharField("ИНН плательщика", max_length=12)
    document_number = models.CharField("Номер документа", max_length=32)
    document_date = models.DateTimeField("Дата документа")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.operation_id}"
