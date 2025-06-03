from django.db import models


class Customer(models.Model):
    customer_external_id = models.IntegerField(
        unique=True, blank=True, null=True
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        max_length=255, unique=True, blank=True, null=True
    )
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    customer_group = models.CharField(max_length=255, blank=True, null=True)
    customer_since = models.DateTimeField(blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    last_order = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_active(self):
        return self.total_orders_count > 0

    @property
    def total_orders_count(self):
        return self.buy_order_detail.count()

    @property
    def total_orders_amount(self):
        return (
            self.buy_order_detail.aggregate(
                total_amount=models.Sum('total_amount')
            )['total_amount']
            or 0.00
        )

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['cpf']),
            models.Index(fields=['cpf', 'email']),
        ]

    def __str__(self):
        return self.email
