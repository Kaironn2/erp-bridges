from source_m.models import PaymentType


class PaymentTypeRepository:
    def get_or_create_by_name(self, name: str) -> PaymentType:
        payment_type_instance, created = PaymentType.objects.get_or_create(name=name)
        return payment_type_instance
