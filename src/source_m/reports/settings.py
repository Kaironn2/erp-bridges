class OrdersReportHandlerSettings:
    columns_mapping = {
        'pedido #': 'buy_order',
        'id do pedido': 'buy_order_external_id',
        'firstname': 'first_name',
        'lastname': 'last_name',
        'email': 'email',
        'grupo do cliente': 'customer_group',
        'número cpf/cnpj': 'cpf',
        'comprado em': 'buy_order_date',
        'shipping telephone': 'phone',
        'status': 'status',
        'número do rastreador': 'tracking_code',
        'qtd. vendida': 'sold_quantity',
        'frete': 'shipping_amount',
        'desconto': 'discount',
        'payment type': 'payment_type',
        'total da venda': 'total_amount',
    }
    currency_columns = ['discount', 'shipping_amount', 'total_amount']
    date_columns = ['buy_order_date']
    numeric_columns = ['cpf', 'phone']
    lowercase_columns = [
        'firstname', 'lastname', 'email', 'customer_group',
        'status', 'payment_type',
    ]
    required_columns = list(columns_mapping.values())
