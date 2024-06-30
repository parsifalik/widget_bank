"""
В этом модуле реализованы две функции, тестирующие 2 функции из модуля:
    "src/processing", "filter_by_state, sort_by_date"
"""

from src.processing import filter_by_state, sort_by_date


def test_sort_logs_by_date(logs_data, sort_logs_by_date_true, sort_logs_by_date_false):
    """
    Сортировка логов по дате статус "TRUE/FALSE".
    :param logs_data: Подаваемые логи в тестируемую функцию: src/processing -> sort_by_date.
    :param sort_logs_by_date_true: Статус TRUE сортирует от большего к меньшему.
    :param sort_logs_by_date_false: Статус FALSE сортирует от меньшему к большего.
    """
    state_true = True
    state_false = False
    assert sort_by_date(logs_data, state_true) == sort_logs_by_date_true
    assert sort_by_date(logs_data, state_false) == sort_logs_by_date_false


def test_filter_by_state(logs_data, filter_by_logs_state_executed, filter_by_logs_state_canceled):
    """
    Тест функции на предмет логов по статусу.
    :param logs_data: Фикстура логов.
    :param filter_by_logs_state_executed: Фикстура для сравнения того что отдаст тестируемая функция статус 'EXECUTED'.
    :param filter_by_logs_state_canceled: То же самое что описано выше, но по статусу 'CANCELED'.
    """
    state_canceled = "CANCELED"
    state_executed = "EXECUTED"
    assert filter_by_state(logs_data, state_executed) == filter_by_logs_state_executed
    assert filter_by_state(logs_data, state_canceled) == filter_by_logs_state_canceled
    assert filter_by_state([], "") == ""
