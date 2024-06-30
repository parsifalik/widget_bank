"""
Модуль содержит функции для тестирования модуля "src/generators".
"""

from unittest.mock import patch

import pytest

from src.generators import card_number_generator, filter_by_description, filter_by_currency
from src.resources import get_logs


@pytest.mark.parametrize(
    "code, expected",
    [
        ("USD", ["939719570", "142264268", "895315941"]),
        ("RUB", ["873106923", "594226727"]),
        ("", ""),
        ("i", "")
    ]
)
def test_filter_by_identifier(code, expected):
    """
    Функция тестирует id операции
    :param code: Код валюты.
    :param expected: id операции
    """
    logs = get_logs()
    identifier_currency = filter_by_currency(logs, code)
    for id_operation in expected:
        assert str(next(identifier_currency)) == id_operation


# тест описание операции от кого и кому
@pytest.mark.parametrize(
    "log, expected",
    [
        (
            get_logs(),
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        )
    ],
)
def test_filter_by_description(log, expected):
    """
    Функция тестирует описание операции.
    :param log: Выполненные логи, приходят от "src/resources".
    :param expected: Описание операции "перевод от кого и кому".
    """
    description = filter_by_description(log)
    for desc in expected:
        assert str(next(description)) == desc


def test_card_number_cenerator():
    """
    Функция тестирует генерацию карт, реализована подмена данных, для корректного тестирования,
    в модуле "src/generators.py" функции "card_number_generator".
    """
    with patch("src.generators.random.randint", return_value=5):
        quantity = 5
        card_number = "5555 5555 5555 5555"
        card_numbers = card_number_generator(quantity, 0, 9)
        for card in card_numbers:
            assert card == card_number
