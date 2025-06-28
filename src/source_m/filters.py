from django.db.models import CharField, Value
from django.db.models.functions import Concat


def filter_customers(queryset, params):
    name = params.get('name')
    customer_group = params.get('customer_group')

    if name:
        queryset = queryset.annotate(
            full_name=Concat(
                'first_name', Value(' '), 'last_name', output_field=CharField()
            )
        ).filter(full_name__icontains=name)

    if customer_group:
        queryset = queryset.filter(customer_group=customer_group)

    return queryset
