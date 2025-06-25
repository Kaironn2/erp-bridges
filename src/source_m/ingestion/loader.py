import pandas as pd

from core.utils.parsers import xml_2003_parser

LOADERS = {
    'customers': xml_2003_parser,
    'orders': xml_2003_parser,
}


def load_data(report_type: str, source_path: str) -> pd.DataFrame:
    loader_fn = LOADERS.get(report_type)
    if not loader_fn:
        raise ValueError(f'No loader defined for {report_type}')
    return loader_fn(source_path)
