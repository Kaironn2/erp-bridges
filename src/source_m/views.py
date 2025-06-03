from http import HTTPStatus

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View


class CustomerView(View):

    def get(self, request: HttpRequest) -> HttpResponse:    # noqa: PLR6301
        context = ...
        return render(request, 'source_m/customers-list', context)

    def post(self, request: HttpRequest) -> HttpResponse:
        pass

    def export_xlsx(self, request: HttpRequest) -> HttpResponse:
        pass
