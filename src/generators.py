import random
from typing import Any, Dict, Generator, List


def filter_by_identifier(transaction_id: List[Dict[str, Any]], currency: str) -> Generator[str, None, None]:
    """
    функция генератор принимает список словарей(логи), и выдает id операции
    :param transaction_id: принимает логи в виде списка словарей
    :param currency: принимает по умолчанию код валюты "USD"
    :yield: возвращает id операции в виде "939719570"
    """
    for item in transaction_id:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item["id"]


def filter_by_description(logs: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    функция генератор принимает список словарей(логи), и выдает описание операции "перевод от кого и кому"
    :param logs: принимает логи в виде списка словарей
    :yield: возвращает описание операции "перевод от кого и кому"
    """
    for item in logs:
        yield item["description"]


def card_number_generator(quantity: int, start: int, stop: int) -> Generator[str, None, None]:
    """
    функция генератор принимает диапазон значений в виде целых чисел
    :param quantity: принимает по умолчанию 5
    :param start: принимает по умолчанию 0
    :param stop: принимает по умолчанию 9
    :yield: возвращает номера случайных карт в виде "1810 7415 0244 8277"
    """
    for amount in range(quantity):
        card = ""
        for num in range(1, 17):
            if num in [5, 9, 13]:
                card += " "
            card += str(random.randint(start, stop))

        yield card
