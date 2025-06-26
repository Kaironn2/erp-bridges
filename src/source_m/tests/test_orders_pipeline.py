import pandas as pd

from source_m.ingestion.loader import LOADERS
from source_m.ingestion.pipeline import SourceMPipeline
from source_m.reports.orders_report import OrdersReportHandler  # noqa: F401


def test_pipeline_with_mocked_data():
    df = pd.DataFrame({
        'Pedido #': ['123'],
        'ID do Pedido': ['A1'],
        'Firstname': ['João'],
        'Lastname': ['Silva'],
        'Email': ['joao@email.com'],
        'Grupo do Cliente': ['Varejo'],
        'Número CPF/CNPJ': ['123.456.789-00'],
        'Comprado em': ['2024-06-01'],
        'Shipping Telephone': ['(11) 91234-5678'],
        'Status': ['Enviado'],
        'Número do Rastreador': ['BR123456789'],
        'Qtd. Vendida': [1],
        'Frete': ['R$ 12,90'],
        'Desconto': ['R$ 5,00'],
        'Payment Type': ['Pix'],
        'Total da Venda': ['R$ 100,00'],
    })

    LOADERS['source_m_orders'] = lambda _: df

    pipeline = SourceMPipeline(
        report_type='source_m_orders', source_path='fake/path.xml'
    )
    result_df = pipeline.run()

    assert not result_df.empty
    assert 'cpf' in result_df.columns
    assert result_df['cpf'].iloc[0] == '12345678900'
