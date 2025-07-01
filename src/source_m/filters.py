import datetime

from django.db.models import CharField, Value
from django.db.models.functions import Concat

from core.utils.cleaners import extract_digits


def filter_customers(queryset, params: dict):
    name = params.get('name')
    customer_group = params.get('customer_group')
    start_date = params.get('start_date')
    end_date = params.get('end_date')
    email = params.get('email')
    cpf = params.get('cpf')

    if name:
        queryset = queryset.annotate(
            full_name=Concat(
                'first_name', Value(' '), 'last_name', output_field=CharField()
            )
        ).filter(full_name__icontains=name)

    if email:
        queryset = queryset.filter(email__icontains=email)

    if cpf:
        cpf = extract_digits(cpf)
        queryset = queryset.filter(cpf__icontains=cpf)

    if customer_group:
        queryset = queryset.filter(customer_group__name=customer_group)

    if start_date:
        try:
            print('START_DATE -> ', start_date)
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            queryset = queryset.filter(last_order__gte=start_date)
        except ValueError:
            print('DEU ERRO!')

    if end_date:
        try:
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
            queryset = queryset.filter(last_order__lte=end_date)
        except ValueError:
            ...

    return queryset
