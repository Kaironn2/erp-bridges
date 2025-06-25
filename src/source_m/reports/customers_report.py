from core.reports.base import BaseReportHandler
from core.reports.registry import register_handler


@register_handler('source_m_customers')
class CustomersReportHandler(BaseReportHandler):

    def preprocess(self):
        return super().preprocess()

    def validate(self):
        return super().validate()

    def transform(self):
        return super().transform()
