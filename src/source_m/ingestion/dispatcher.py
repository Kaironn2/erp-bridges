from core.reports.registry import REPORT_HANDLERS


def get_handler_class(report_type: str):
    handler_cls = REPORT_HANDLERS.get(report_type)
    if not handler_cls:
        raise ValueError(f'No handler defined for {report_type}')
    return handler_cls
