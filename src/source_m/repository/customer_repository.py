from source_m.models import Customer


class CustomerRepository:
    def bulk_create(self, customers: list[Customer], batch_size: int):
        Customer.objects.bulk_create(customers, batch_size=batch_size)

    def bulk_update(self, customers: list[Customer], fields: list, batch_size: int):
        Customer.objects.bulk_update(customers, fields=fields, batch_size=batch_size)

    def create(self, data):
        Customer.objects.create(**data)

    def get_by_cpf(self, cpf):
        return Customer.objects.filter(cpf=cpf).first()

    def get_by_email(self, email):
        return Customer.objects.filter(email=email).first()
