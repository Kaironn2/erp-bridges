from source_m.models import CustomerGroup


class CustomerGroupRepository:
    def get_or_create_by_name(self, name: str) -> CustomerGroup:
        customer_group_instance, created = CustomerGroup.objects.get_or_create(
            name=name
        )
        return customer_group_instance
