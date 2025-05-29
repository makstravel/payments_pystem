from django.db import transaction
from apps.organizations.models import Organization, BalanceLog
from apps.payments.models import Payment

def process_bank_webhook(data: dict) -> bool:
    """
    Обрабатывает банковский webhook:
    - Если операция уже есть (operation_id) — ничего не делает, возвращает False.
    - Если новая операция — создаёт Payment, увеличивает баланс организации и логирует изменение.
    :param data: Данные из webhook (валидированные)
    :return: True — если платеж проведён; False — если дубль
    """
    with transaction.atomic():
        operation_id = data['operation_id']

        # Защита от дублей по operation_id
        if Payment.objects.filter(operation_id=operation_id).exists():
            return False

        # Создание платежа
        payment = Payment.objects.create(**data)

        # Поиск или создание организации по ИНН
        org, created = Organization.objects.get_or_create(
            inn=data['payer_inn'],
            defaults={'balance': 0}
        )

        # Начисление баланса
        org.balance += data['amount']
        org.save()

        # Логирование изменения баланса
        BalanceLog.objects.create(
            organization=org,
            amount=data['amount'],
            operation_id=operation_id
        )

    return True
