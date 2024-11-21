from datetime import datetime


def timestamp_to_date(timestamp: int, custom_format: str) -> str:
    """Convertit un timestamp en une chaîne de caractères,
    en fonction d'une chaîne de format."""
    return datetime.fromtimestamp(timestamp).strftime(custom_format)
