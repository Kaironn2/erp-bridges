import io

from django.core.paginator import Paginator
from django.db.models import CharField, Value
from django.db.models.functions import Concat
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.views.generic import View
from openpyxl import Workbook

from source_m.models import Customer


class CustomerListExportView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        if request.GET.get('export') == '1':
            return self.export_xlsx(request=request)

        name = request.GET.get('name')
        customer_group = request.GET.get('customer_group')

        queryset = Customer.objects.all()

        if name:
            queryset = queryset.annotate(
                full_name=Concat(
                    'first_name', Value(' '), 'last_name', output_field=CharField()
                )
            ).filter(full_name__icontains=name)

        if customer_group:
            queryset = queryset.filter(customer_group=customer_group)

        paginator = Paginator(queryset, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        customer_groups = Customer.objects.exclude(
            customer_group=''
        ).values_list('customer_group', flat=True).distinct()

        context = {
            'page_obj': page_obj,
            'customer_groups': customer_groups,
        }
        return render(request, 'source_m/customers-list.html', context)

    def export_xlsx(self, request: HttpRequest) -> HttpResponse:
        name = request.GET.get('name')
        customer_group = request.GET.get('customer_group')

        queryset = Customer.objects.all()

        if name:
            queryset = queryset.annotate(
                full_name=Concat(
                    'first_name', Value(' '), 'last_name', output_field=CharField()
                )
            ).filter(full_name__icontains=name)

        if customer_group:
            queryset = queryset.filter(customer_group=customer_group)

        wb = Workbook()
        ws = wb.active
        ws.title = 'Clientes'

        headers = ['Nome', 'E-mail', 'CPF', 'Grupo', 'Última Compra', 'Telefone']
        ws.append(headers)

        for customer in queryset:
            full_name = f'{customer.first_name} {customer.last_name}'
            ws.append([
                smart_str(full_name),
                smart_str(customer.email),
                smart_str(customer.cpf),
                smart_str(customer.customer_group),
                customer.last_order.strftime('%d/%m/%Y') if customer.last_order else '',
                smart_str(customer.phone),
            ])

        buffer = io.BytesIO()
        wb.save(buffer)
        buffer.seek(0)

        response = HttpResponse(
            buffer,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=clientes.xlsx'
        return response
