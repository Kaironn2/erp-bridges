import re


def extract_digits(text_input) -> str | None:
    if not text_input:
        return None
    return re.sub(r'\D', '', str(text_input))
