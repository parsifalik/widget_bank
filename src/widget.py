"""
В этом модуле функция "get_mask_card_and_mask_pay" принимает данные о карте пользователя обрабатывает и
возвращает данные карты/счета в формате хххх хх** **** хххх/**хххх
"""


def get_mask_card_and_mask_pay(card_and_pay: str) -> str:
    """
    Функция принимает номер карты/счета, возвращает маску карты/счета.
    :param card_and_pay: Строка из цифр.
    :return: Маскированные данные карты/счета.
    """
    if card_and_pay:
        payment_number_incoming = ""
        payment_number = ""
        for elem in card_and_pay:
            if elem.isdigit():
                payment_number_incoming += elem
        if len(payment_number_incoming) == 16:
            payment_number += (
                f"{payment_number_incoming[:4]} {payment_number_incoming[6:8]}** **** {payment_number_incoming[-4:]}"
            )
        elif len(payment_number_incoming) == 20:
            payment_number += f"**{payment_number_incoming[-4:]}"
        return payment_number
    return ""
