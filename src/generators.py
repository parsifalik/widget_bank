"""
В этом модуле содержатся функции для возврата (id операции), (описание операции), (генерации карт).
"""

import random
from typing import Any, Dict, Generator, List


def filter_by_currency(transaction_id: List[Dict[str, Any]], currency: str) -> Generator[str, None, None]:
    """
    Функция генератор принимает список словарей(логи).
    :param transaction_id: Логи в виде списка словарей.
    :param currency: По умолчанию код валюты "USD".
    :yield: id операции в виде "939719570".
    """
    for item in transaction_id:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item["id"]


def filter_by_description(logs: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    Функция генератор принимает список словарей(логи).
    :param logs: Логи в виде списка словарей.
    :yield: Описание операции "перевод от кого и кому".
    """
    for item in logs:
        yield item["description"]


def card_number_generator(quantity: int, start: int, stop: int) -> Generator[str, None, None]:
    """
    Функция генератор принимает диапазон значений в виде целых чисел.
    :param quantity: Кол - во генерации.
    :param start: По умолчанию 0.
    :param stop: По умолчанию 9.
    :yield: Номера случайных карт в виде "1810 7415 0244 8277".
    """
    for _ in range(quantity):
        card = ""
        for num in range(1, 17):
            if num in [5, 9, 13]:
                card += " "
            card += str(random.randint(start, stop))

        yield card
