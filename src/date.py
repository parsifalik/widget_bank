"""
Модуль для возврата системной даты в формате хх.хх.ххх.
"""

from datetime import datetime


def get_date() -> str:
    """
    Мини функция возвращающая системную дату устройства.
    :return: Дату в формате 05.04.1994.
    """
    return datetime.now().strftime("%d.%m.%y")
