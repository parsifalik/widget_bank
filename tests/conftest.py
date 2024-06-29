"""
В этом модуле содержатся фикстуры тестов для модуля "test_processing.py".
"""

import pytest


@pytest.fixture
def logs_data():
    """
    Фикстура подачи данных для тестирования в функцию:
        test_filter_by_state.
    :return: Список словарей(логи).
    """
    logs = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return logs


#######################################################################################################################


@pytest.fixture
def filter_by_logs_state_executed() -> str:
    """
    Фикстура для сравнения данных, тестируемой функции:
        в src/processing -> filter_by_state,
        по статусу "EXECUTED".
    :return: Строка деленная на два блока (executed)(canceled).
    """
    logs_executed = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    logs_canceled = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return f"{logs_executed}\n    {logs_canceled}"


@pytest.fixture
def filter_by_logs_state_canceled() -> str:
    """
    Фикстура для сравнения данных тестируемой функции:
        в src/processing -> filter_by_state,
        по статусу "CANCELED".
    :return: Строка деленная на два блока (canceled)(executed).
    """
    logs_canceled = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    logs_executed = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return f"{logs_canceled}\n    {logs_executed}"


#######################################################################################################################


@pytest.fixture
def sort_logs_by_date_true():
    """
    Фикстура для сравнения данных тестируемой функции:
        в src/processing -> sort_by_date,
        сортировка по умолчанию True.
    :return: Данные от большей даты к меньшей.
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_logs_by_date_false():
    """
    Фикстура для сравнения данных тестируемой функции:
        в src/processing -> sort_by_date,
        сортировка по умолчанию False.
    :return: Данные от меньшей даты к большей
    """
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
