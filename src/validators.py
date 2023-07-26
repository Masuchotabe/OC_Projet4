import re


def validate_date_from_str(string_to_validate):
    pattern = r"[0-3]?\d/[0-2]?\d/\d{4}"
    return re.match(pattern, string_to_validate)

def validate_national_chess_identifier(string_to_validate):
    pattern = r"[a-zA-Z]{2}\d{5}"
    return re.match(pattern, string_to_validate)