REPORT_HANDLERS = {}


def register_handler(report_type: str):
    def decorator(cls):
        if report_type in REPORT_HANDLERS:
            raise ValueError(f'Handler already registered for "{report_type}"')
        REPORT_HANDLERS[report_type] = cls
        return cls
    return decorator
