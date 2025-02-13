import time
from zoneinfo import ZoneInfo
from datetime import datetime
from tzlocal import get_localzone
from typing import Iterator, Tuple



def get_fiestas_patrias() -> datetime:
    """Retorna la fecha de las próximas Fiestas Patrias en Santiago de 
    Chile."""
    # defino     
    santiago_timezone = ZoneInfo("America/Santiago")
    user_datetime = datetime.now(get_localzone())
    user_datetime_chl = user_datetime.astimezone(santiago_timezone)

    fiestas_patrias = datetime(user_datetime_chl.year, 9, 18,
                               tzinfo=(santiago_timezone))

    if user_datetime_chl >= fiestas_patrias:
        fiestas_patrias = datetime(user_datetime_chl.year + 1, 9, 18,
                                   tzinfo=(santiago_timezone))

    return fiestas_patrias


def timer() -> Iterator[Tuple[int, int, int, int]]:
    """Calcula el tiempo restante hasta las Fiestas Patrias y lo retorna
    como tupla. Si el tiempo llega a cero, recalcula la próxima fecha de 
    Fiestas Patrias."""
    fiestas_patrias = get_fiestas_patrias()

    while True:
        santiago_timezone = ZoneInfo("America/Santiago")
        user_datetime = datetime.now(get_localzone())
        user_datetime_chl = user_datetime.astimezone(santiago_timezone)
       
        countdown = fiestas_patrias - user_datetime_chl

        if countdown.total_seconds() <= 0:
            fiestas_patrias = get_fiestas_patrias()
            continue

        days = countdown.days
        hours, reminder = divmod(countdown.seconds, 3600)
        minutes, seconds = divmod(reminder, 60)

        yield days, hours, minutes, seconds
        time.sleep(1)



if __name__ == "__main__":
    def main() -> None:
        try:
            for days, hours, minutes, seconds in timer():
                print(f"{days} días {hours:02}:{minutes:02}:{seconds:02}",
                      "¡para las fiestas patrias! 🎉",
                    end="\r")
        except KeyboardInterrupt:
            print("\nContador detenido")
    main()
