"""
В этом модуле две функции, первая обрабатывает статус выполнения, вторая обрабатывает статус даты выполнения.
"""

from typing import Dict, List


def filter_by_state(list_dict: List[Dict], state: str) -> str:
    """
    Принимает логи в виде списка словарей.
    :param list_dict: Список словарей(логи) выполненных и отмененных операций.
    :param state: Статус по умолчанию EXECUTED, можно изменить из главного модуля.
    :return: Строка, деленная на два блока со статусом EXECUTED и CANCELED.
    """
    result_executed = []
    result_canceled = []
    total_result = ""
    for item in list_dict:
        if item.get("state") == "EXECUTED":
            result_executed.append(item)
        elif item.get("state") == "CANCELED":
            result_canceled.append(item)
    if str(state) == "EXECUTED":
        total_result = f"{result_executed}\n    {result_canceled}"
    elif str(state) == "CANCELED":
        total_result = f"{result_canceled}\n    {result_executed}"
    return str(total_result)


def sort_by_date(list_dict: list[Dict], sort) -> List[Dict]:
    """
    Принимает логи в виде списка словарей.
    :param list_dict: Список словарей(логи) выполненных, и отмененных операций.
    :param sort: Сортировка по умолчанию=True, можно изменить из главного модуля.
    :return: Возвращает список словарей, отсортированных от большего к меньшему, в зависимости статуса по умолчанию.
    """
    list_dict_sorted = sorted(list_dict, key=lambda x: x["date"], reverse=sort)
    return list_dict_sorted
