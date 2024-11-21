from datetime import datetime, timedelta

SECONDS_IN_A_DAY = 86400


def find_tomorrow_timestamp_range() -> list[int]:
    """Renvoie une liste de deux timestamps, qui représentent respectivement
    le début et la fin du lendemain."""

    tomorrow = datetime.today() + timedelta(days=1)
    tomorrow_start = tomorrow.replace(hour=0, minute=0, second=0)
    tomorrow_end = tomorrow.replace(hour=23, minute=59, second=59)
    return [int(tomorrow_start.timestamp()), int(tomorrow_end.timestamp())]


def timestamp_range_for_the_next_fives_days(start_range=None) -> list[list[int]]:
    """Renvoie une liste de 5 plages de timestamps, qui représentent respectivement
    les 5 prochains jours. Chaque plage est une liste de deux timestamps,
    qui représentent respectivement le début et la fin du jour.
    """
    if start_range is None:
        start_range = find_tomorrow_timestamp_range()
    return [
        [start_range[0] + i * SECONDS_IN_A_DAY, start_range[1] + i * SECONDS_IN_A_DAY]
        for i in range(5)
    ]
