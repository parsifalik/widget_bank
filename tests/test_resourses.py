"""
В этом модуле тестируется модуль src/resources.py на отдачу списка словарей
"""

from src.resources import get_logs
log = get_logs()


def test_logs():
    """
    Функция для проверки корректного возврата списка словарей(логи)
    """
    assert get_logs() == log
