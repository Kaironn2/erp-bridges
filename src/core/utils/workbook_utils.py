import io

from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet


class WorkBookUtils:

    @staticmethod
    def adjust_columns_width(worksheet: Worksheet):
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if cell.value is not None:
                        cell_length = len(str(cell.value))
                        max_length = max(max_length, cell_length)
                except TypeError:
                    pass
            adjusted_width = (max_length + 2)
            worksheet.column_dimensions[column_letter].width = adjusted_width

    @staticmethod
    def generate_excel_response(
        headers: list[str],
        data: list[list],
        filename: str = 'export.xlsx',
        sheet_title: str = 'Sheet1'
    ) -> HttpResponse:
        wb = Workbook()
        ws = wb.active
        ws.title = sheet_title

        ws.append(headers)

        for row_data in data:
            ws.append(row_data)

        WorkBookUtils.adjust_columns_width(ws)

        buffer = io.BytesIO()
        wb.save(buffer)
        buffer.seek(0)

        response = HttpResponse(
            buffer,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
