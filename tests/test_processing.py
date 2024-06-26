from src.processing import filter_by_state, sort_by_date


def test_sort_logs_by_date(logs_data, sort_logs_by_date_true, sort_logs_by_date_false):
    """
    тест сортировки логов по дате статус "TRUE/FALSE"
    :param logs_data: подаваемые логи в тестируемую функцию: src/processing -> sort_by_date
    :param sort_logs_by_date_true: статус TRUE сортирует от большего к меньшему
    :param sort_logs_by_date_false: статус FALSE сортирует от меньшему к большего
    """
    state_true = True
    state_false = False
    assert sort_by_date(logs_data, state_true) == sort_logs_by_date_true
    assert sort_by_date(logs_data, state_false) == sort_logs_by_date_false


def test_filter_by_state(logs_data, filter_by_logs_state_executed, filter_by_logs_state_canceled):
    """
    тест функции на предмет логов по статусу
    :param logs_data: принимает фикстуру логов, и отдает ее в тестируемую функцию
    :param filter_by_logs_state_executed: фикстура для сравнения того что отдаст тестируемая функия статус 'EXECUTED'
    :param filter_by_logs_state_canceled: то же самое что описано выше, но по статусу 'CANCELED'
    """
    state_canceled = "CANCELED"
    state_executed = "EXECUTED"
    assert filter_by_state(logs_data, state_executed) == filter_by_logs_state_executed
    assert filter_by_state(logs_data, state_canceled) == filter_by_logs_state_canceled
    assert filter_by_state([], "") == ""
