from abc import ABC, abstractmethod


class BaseIngestionPipeline(ABC):
    def __init__(self, source_path):
        self.source_path = source_path

    def run(self):
        raw_data = self.load()
        handler_cls = self.get_handler_class()
        handler = handler_cls(raw_data)
        return handler.handle()

    @abstractmethod
    def load(self):
        '''Load raw source'''
        pass

    @abstractmethod
    def get_handler_class(self):
        '''return correspondent handler class'''
        pass
