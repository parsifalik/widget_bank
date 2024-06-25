import pytest
from src.widget import get_mask_card_and_mask_pay


@pytest.mark.parametrize(
    "number_pay_input, number_pay_result",
    [
        ("visa 8888 8888 8888 8888", "8888 88** **** 8888"),
        ("8888888888888888", "8888 88** **** 8888"),
        ("8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8", "8888 88** **** 8888"),
        ("", ""),
    ],
)
def test_number_pay_and_card(number_pay_input, number_pay_result):
    """
    тестирование функции скрытия маски карты/счета:
        src/widget -> get_mask_card_and_mask_pay
    """
    assert get_mask_card_and_mask_pay(number_pay_input) == number_pay_result
    assert get_mask_card_and_mask_pay(number_pay_input) == number_pay_result
