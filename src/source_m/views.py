from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from source_m.models import Customer


class CustomerView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        customers = Customer.objects.all()
        context = {'customers': customers}
        return render(request, 'source_m/customers-list.html', context)

    def post(self, request: HttpRequest) -> HttpResponse:
        pass

    def export_xlsx(self, request: HttpRequest) -> HttpResponse:
        pass
