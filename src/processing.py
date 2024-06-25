from typing import Dict, List


def filter_by_state(list_dict: List[Dict], state: str) -> str:
    """
    принимает логи в виде списка словарей
    :param list_dict: принимает на вход список словарей(логи) выполненных и отмененных операций
    :param state: статус по умолчанию EXECUTED, можно изменить из главного модуля
    :return: возвращает строку деленную на две строки со статусом EXECUTED и CANCELED
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
    принимает логи в виде списка словарей
    :param list_dict: принимает на вход список словарей(логи) выполненных и отмененных операций
    :param sort: сортировка по умолчанию=True можно изменить из главного модуля
    :return: возвращает список словарей отсортированных от большего к меньшему, в зависимости статуса по умолчанию
    """
    list_dict_sorted = sorted(list_dict, key=lambda x: x["date"], reverse=sort)
    return list_dict_sorted
