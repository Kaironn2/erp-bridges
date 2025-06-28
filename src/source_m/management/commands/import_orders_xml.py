from django.core.management.base import BaseCommand

from source_m.ingestion.pipeline import SourceMPipeline
from source_m.reports.orders_report import OrdersReportHandler  # noqa: F401


class Command(BaseCommand):
    help = 'process buy orders xml'

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            type=str,
            required=True,
            help='.xml file path'
        )

    def handle(self, *args, **options):
        path = options['path']
        pipeline = SourceMPipeline('source_m_orders', path)
        pipeline.run()
