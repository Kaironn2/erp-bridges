from typing import Any, Dict, List

import pandas as pd
from django.utils.timezone import make_aware


class Dataframeutils:
    @staticmethod
    def str_currency_to_float(
        df: pd.DataFrame, columns: List[str], currency: str = 'R$'
    ) -> pd.DataFrame:
        for column in columns:
            if column in df.columns:
                df[column] = (
                    df[column]
                    .astype(str)
                    .str.replace(currency, '', regex=False)
                    .str.replace('.', '', regex=False)
                    .str.replace(',', '.', regex=False)
                    .astype(float)
                )
        return df

    @staticmethod
    def clean_numeric_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        for column in columns:
            if column in df.columns:
                df[column] = df[column].str.replace(r'[^\d]', '', regex=True)
        return df

    @staticmethod
    def lowercase_columns(df: pd.DataFrame, columns: List[str]) -> None:
        for column in columns:
            if column in df.columns:
                df[column] = df[column].str.lower()
        return df

    @staticmethod
    def str_to_date(
        df: pd.DataFrame, columns: List[str], input_format: str = None
    ) -> pd.DataFrame:
        for col in columns:
            df[col] = pd.to_datetime(df[col], format=input_format, errors='coerce')
            df[col] = df[col].apply(
                lambda dt: make_aware(dt)
                if pd.notnull(dt) and dt.tzinfo is None else dt
            )
        return df

    @staticmethod
    def replace_values(
        df: pd.DataFrame, replacers: Dict[str, Dict[Any, Any]], contains: bool = False
    ) -> pd.DataFrame:
        df_copy = df.copy()
        for column, replacements in replacers.items():
            if column not in df.columns:
                raise ValueError(f'Error: Column {column} not found in DataFrame.')

            for original_value, new_value in replacements.items():
                if contains:
                    mask = df_copy[column].astype(str).str.contains(
                        str(original_value), na=False
                    )
                    df_copy.loc[mask, column] = new_value
                else:
                    df_copy[column] = df_copy[column].replace(original_value, new_value)

        return df_copy
