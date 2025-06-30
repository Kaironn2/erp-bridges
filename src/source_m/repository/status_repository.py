from source_m.models import Status


class StatusRepository:
    def get_or_create_by_name(self, name: str) -> Status:
        payment_type_instance, created = Status.objects.get_or_create(name=name)
        return payment_type_instance
