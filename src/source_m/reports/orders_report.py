import pandas as pd

from core.reports.base import BaseReportHandler
from core.reports.registry import register_handler
from core.utils.dataframe_utils import Dataframeutils as dft
from source_m.services.customer_service import CustomerService

from .settings import OrdersReportHandlerSettings


@register_handler('source_m_orders')
class OrdersReportHandler(BaseReportHandler, OrdersReportHandlerSettings):
    def preprocess(self):
        df = self.raw_data

        df.columns = df.columns.str.lower()
        df = df.rename(columns=self.columns_mapping)
        df = dft.str_to_date(df, self.date_columns, input_format='%d/%m/%Y %H:%M:%S')
        df = dft.lowercase_columns(df, self.lowercase_columns)
        df = dft.clean_numeric_columns(df, self.numeric_columns)
        df = dft.str_currency_to_float(df, self.currency_columns)
        self.clean_data = df

    def validate(self):
        if self.clean_data.empty:
            raise ValueError('Dataframe is empty after preprocessing')

        missing = [
            col for col in self.required_columns if col not in self.clean_data.columns
        ]
        if missing:
            raise ValueError(f'Missing required columns {missing}')

        for col in self.currency_columns:
            if not pd.api.types.is_numeric_dtype(self.clean_data[col]):
                raise TypeError(f'Column "{col}" isnt in numeric format')

    def transform(self):
        customer_service = CustomerService()
        customer_service.upsert_customers(self.clean_data)
        return self.clean_data
