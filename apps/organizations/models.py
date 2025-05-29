from django.db import models

class Organization(models.Model):
    """Модель организации с балансом."""
    inn = models.CharField("ИНН", max_length=12, unique=True, db_index=True)
    balance = models.BigIntegerField("Баланс", default=0)

    def __str__(self):
        return f"Организация ИНН {self.inn}"


class BalanceLog(models.Model):
    """Лог изменения баланса организации."""
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='balance_logs')
    amount = models.BigIntegerField("Сумма изменения")
    operation_id = models.UUIDField("ID операции")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"BalanceLog {self.organization.inn} {self.amount} {self.created_at}"

