from unittest.mock import patch

import pytest

from src.generators import card_number_generator, filter_by_description, filter_by_identifier
from src.resources import get_logs


# тест id операции
@pytest.mark.parametrize("log, expected", [(get_logs(), ["939719570", "142264268", "895315941"])])
def test_filter_by_identifier(log, expected):
    identifier = filter_by_identifier(log, "USD")
    for id_operation in expected:
        assert str(next(identifier)) == id_operation


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
    description = filter_by_description(log)
    for desc in expected:
        assert str(next(description)) == desc


# тест на генерацию карт
def test_card_number_cenerator():
    with patch("src.generators.random.randint", return_value=5):
        quantity = 5
        card_number = "5555 5555 5555 5555"
        card_numbers = card_number_generator(quantity, 0, 9)
        for card in card_numbers:
            assert card == card_number
