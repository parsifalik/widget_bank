"""
В этом модуле функция "test_get_date" тестирует функцию "src/date/get_date" на отдачу даты в формате хх.хх.хххх.
"""

from datetime import datetime

from src.date import get_date


def test_get_date():
    """
    Тестирование функции src/date -> get_date.
    """
    assert get_date() == datetime.now().strftime("%d.%m.%y")
