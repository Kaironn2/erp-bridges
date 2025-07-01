from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.views.generic import View

from core.utils.workbook_utils import WorkBookUtils
from source_m.filters import filter_customers
from source_m.models import Customer, CustomerGroup


class CustomerListExportView(View):
    main_template = 'source_m/customers-list.html'
    table_template = 'source_m/partials/_customers-table.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        if request.GET.get('export') == '1':
            return self.export_xlsx(request=request)

        queryset = filter_customers(Customer.objects.all(), request.GET)

        paginator = Paginator(queryset, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {'page_obj': page_obj}

        if request.htmx:
            return render(request, self.table_template, context)

        context['customer_groups'] = CustomerGroup.objects.all().order_by('name')

        return render(request, self.main_template, context)

    def export_xlsx(self, request: HttpRequest) -> HttpResponse:
        queryset = filter_customers(Customer.objects.all(), request.GET)

        headers = ['Nome', 'E-mail', 'CPF', 'Grupo', 'Última Compra', 'Telefone']

        data_rows = []

        for customer in queryset:
            full_name = f'{customer.first_name} {customer.last_name}'

            group_name = customer.customer_group.name if customer.customer_group else ''
            last_order_str = customer.last_order.strftime(
                '%d/%m/%Y'
            ) if customer.last_order else ''

            data_rows.append([
                smart_str(full_name),
                smart_str(customer.email),
                smart_str(customer.cpf),
                smart_str(group_name),
                last_order_str,
                smart_str(customer.phone),
            ])

        return WorkBookUtils.generate_excel_response(
            headers=headers,
            data=data_rows,
            filename='clientes.xlsx',
            sheet_title='Clientes'
        )
