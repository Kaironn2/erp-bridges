import pandas as pd


class Dataframeutils:
    @staticmethod
    def convert_str_currency_to_float(
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

    def lowercase_columns(df: pd.DataFrame, columns: list[str]) -> None:
        for column in columns:
            if column in df.columns:
                df[column] = df[column].str.lower()
        return df
