from core.ingestion.base import BaseIngestionPipeline
from source_m.ingestion.dispatcher import get_handler_class
from source_m.ingestion.loader import load_data


class SourceMPipeline(BaseIngestionPipeline):
    def __init__(self, report_type, source_path):
        super().__init__(source_path)
        self.report_type = report_type

    def load(self):
        return load_data(self.report_type, self.source_path)

    def get_handler_class(self):
        return get_handler_class(self.report_type)
