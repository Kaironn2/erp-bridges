import pandas as pd

from core.reports.base import BaseReportHandler
from core.reports.registry import register_handler
from core.utils.dataframe_utils import Dataframeutils as dft


@register_handler('source_m_orders')
class OrdersReportHandler(BaseReportHandler):
    numeric_columns = ['número cpf/cnpj', 'shipping telephone']
    currency_columns = ['desconto', 'frete', 'total da venda']
    lowercase_columns = [
        'firstname', 'lastname', 'email', 'grupo do cliente',
        'status', 'payment type',
    ]
    required_columns = [
        'pedido #', 'id do pedido', 'firstname', 'lastname',
        'email', 'grupo do cliente', 'número cpf/cnpj', 'comprado em',
        'shipping telephone', 'status', 'número do rastreador', 'qtd. vendida',
        'frete', 'desconto', 'payment type', 'total da venda'
    ]

    def preprocess(self):
        df = self.raw_data

        df.columns = df.columns.str.lower()
        df = dft.lowercase_columns(df, self.lowercase_columns)
        df = dft.clean_numeric_columns(df, self.numeric_columns)
        df = dft.convert_str_currency_to_float(df, self.currency_columns)
        self.raw_data = df

    def validate(self):
        if self.raw_data.empty:
            raise ValueError('Dataframe is empty after preprocessing')

        missing = [
            col for col in self.required_columns if col not in self.raw_data.columns
        ]
        if missing:
            raise ValueError(f'Missing required columns {missing}')

        for col in self.currency_columns:
            if not pd.api.types.is_numeric_dtype(self.raw_data[col]):
                raise TypeError(f'Column "{col}" isnt in numeric format')

    def transform(self):
        return self.raw_data
