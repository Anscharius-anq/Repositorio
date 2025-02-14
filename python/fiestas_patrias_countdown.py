import time
from zoneinfo import ZoneInfo
from datetime import datetime
from tzlocal import get_localzone
from typing import Iterator, Tuple


def get_fiestas_patrias() -> datetime:
    """Retorna la fecha de las próximas Fiestas Patrias en Santiago de 
    Chile."""

    santiago_timezone = ZoneInfo("America/Santiago")
    # Obtener y convertir fecha/hora la zona horaria del usuario a la de Chile
    user_datetime = datetime.now(get_localzone())
    user_datetime_chl = user_datetime.astimezone(santiago_timezone)

    # Definir la fecha de las próximas Fiestas Patrias (18 de septiembre)
    fiestas_patrias = datetime(user_datetime_chl.year, 9, 18,
                               tzinfo=(santiago_timezone))

    # evaluar si pasó el 18 de este año, calcular para el próximo año
    if user_datetime_chl >= fiestas_patrias:
        fiestas_patrias = datetime(user_datetime_chl.year + 1, 9, 18,
                                   tzinfo=(santiago_timezone))

    return fiestas_patrias


def timer() -> Iterator[Tuple[int, int, int, int]]:
    """Calcula el tiempo restante hasta las Fiestas Patrias y lo retorna
    como tupla. Si el tiempo llega a cero, recalcula la próxima fecha de 
    Fiestas Patrias."""

    # Obtener la fecha de las próximas Fiestas Patrias
    fiestas_patrias = get_fiestas_patrias()
    santiago_tz = ZoneInfo("America/Santiago")

    while True:
        # Obtener la fecha y hora actual en la zona horaria del usuario
        # y convertirla a Santiago
        user_datetime = datetime.now(get_localzone()).astimezone(santiago_tz)
        countdown = fiestas_patrias - user_datetime

        # Si el tiempo ha llegado a 0, recalcular la próxima fecha y continuar
        if countdown.total_seconds() <= 0:
            fiestas_patrias = get_fiestas_patrias()
            continue

        # Extraer los días, horas, minutos y segundos del timedelta resultante
        days = countdown.days
        hours, reminder = divmod(countdown.seconds, 3600)
        minutes, seconds = divmod(reminder, 60)

        # Retornar los valores como una tupla
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
