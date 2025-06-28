from django.urls import path

from .views import CustomerListExportView

urlpatterns = [
    path('customers/', CustomerListExportView.as_view(), name='source-m-customers-list')
]
