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
    """
    Renvoie une liste de 5 listes de timestamps, qui représentent respectivement le début et la fin de 5 jours consécutifs,
    en partant de la plage de timestamps fournie en argument.

    Chaque élément de la liste renvoyée contient deux timestamps, qui représentent le début et la fin d'un jour.
    La méthode fonctionne en ajoutant 24h à chaque itération, en partant du premier timestamp de la liste d'origine.
    """
    if start_range is None:
        start_range = find_tomorrow_timestamp_range()
    increase_by = 0
    result = []
    for _ in range(5):
        result.append(list(map(lambda x, inc=increase_by: x + inc, start_range)))
        increase_by += SECONDS_IN_A_DAY
    return result
