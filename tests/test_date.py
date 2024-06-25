from datetime import datetime
from src.date import get_date


def test_get_date():
    """
    тестирование функции src/date -> get_date
    """
    assert get_date() == datetime.now().strftime("%d.%m.%y")
