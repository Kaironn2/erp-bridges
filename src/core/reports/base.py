from abc import ABC, abstractmethod

import pandas as pd


class BaseReportHandler(ABC):
    def __init__(self, raw_data):
        self.raw_data: pd.DataFrame = raw_data

    def handle(self):
        self.preprocess()
        self.validate()
        return self.transform()

    def preprocess(self):
        pass

    def validate(self):
        pass

    @abstractmethod
    def transform(self):
        raise NotImplementedError('The "transform" method must be implemented')
