from datetime import datetime, timedelta

SECONDS_IN_A_DAY = 86400


def find_tomorrow_timestamp_range():
    """
    Renvoie un tuple de deux timestamps, qui représentent respectivement le début et la fin du lendemain.

    La méthode fonctionne en ajoutant un jour à la date actuelle, puis en créant deux objets datetime :
    - le premier avec l'heure 00h00min00s,
    - le second avec l'heure 23h59min59s.
    Enfin, la méthode renvoie les timestamps correspondants à ces deux objets datetime.
    """
    tomorrow = datetime.today() + timedelta(days=1)
    tomorrow_start = tomorrow.replace(hour=0, minute=0, second=0)
    tomorrow_end = tomorrow.replace(hour=23, minute=59, second=59)
    tomorrow_start_timestamp = int(tomorrow_start.timestamp())
    tomorrow_end_timestamp = int(tomorrow_end.timestamp())
    tomorrow_timestamp_range = [tomorrow_start_timestamp, tomorrow_end_timestamp]
    return tomorrow_timestamp_range
