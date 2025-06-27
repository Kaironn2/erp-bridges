import pandas as pd

from source_m.models import Customer
from source_m.repository.customer_repository import CustomerRepository


class CustomerService:
    def __init__(self):
        self.repository = CustomerRepository()
        self.fields_to_track = [
            'first_name', 'last_name', 'email', 'cpf',
            'phone', 'customer_group', 'last_order'
        ]

    def upsert_customers(self, df: pd.DataFrame) -> None:
        to_create = []
        to_update = []

        for _, row in df.iterrows():
            row_data = row.to_dict()
            row_data['last_order'] = row_data.pop('buy_order_date')

            cpf = row_data.get('cpf')
            email = row_data.get('email')

            customer = self.repository.get_by_email(email=email)
            if not customer:
                customer = self.repository.get_by_cpf(cpf=cpf)

            if customer:
                if self._apply_updates(customer=customer, row_data=row_data):
                    to_update.append(customer)
            else:
                to_create.append(Customer(**{
                    field: row_data.get(field)
                    for field in self.fields_to_track
                }))

        if to_create:
            self.repository.bulk_create(to_create, batch_size=500)

        if to_update:
            self.repository.bulk_update(
                to_update, fields=self.fields_to_track, batch_size=500
            )

    def _apply_updates(self, customer, row_data: dict) -> bool:
        updated_fields = []
        for field in self.fields_to_track:
            new_value = row_data.get(field)
            old_value = getattr(customer, field)

            if field == 'last_order':
                if not old_value or (new_value and new_value > old_value):
                    setattr(customer, field, new_value)
                    updated_fields.append(field)
            elif new_value != old_value:
                setattr(customer, field, new_value)
                updated_fields.append(field)

        return bool(updated_fields)
