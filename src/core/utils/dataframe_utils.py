import pandas as pd
from django.utils.timezone import make_aware


class Dataframeutils:
    @staticmethod
    def str_currency_to_float(
        df: pd.DataFrame, columns: list[str], currency: str = 'R$'
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
    def clean_numeric_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
        for column in columns:
            if column in df.columns:
                df[column] = df[column].str.replace(r'[^\d]', '', regex=True)
        return df

    @staticmethod
    def lowercase_columns(df: pd.DataFrame, columns: list[str]) -> None:
        for column in columns:
            if column in df.columns:
                df[column] = df[column].str.lower()
        return df

    @staticmethod
    def str_to_date(
        df: pd.DataFrame, columns: list[str], input_format: str = None
    ) -> pd.DataFrame:
        for col in columns:
            df[col] = pd.to_datetime(df[col], format=input_format, errors='coerce')
            df[col] = df[col].apply(
                lambda dt: make_aware(dt)
                if pd.notnull(dt) and dt.tzinfo is None else dt
            )
        return df
