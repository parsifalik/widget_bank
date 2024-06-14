from datetime import datetime


def get_date() -> str:
    """
    Мини функция возвращающая системную дату устройства
    :return: возвращает дату в формате 05.04.1994
    """
    return datetime.now().strftime("%d.%m.%y")
