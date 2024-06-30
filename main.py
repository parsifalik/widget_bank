"""программа для скрытия номера карты/счета"""

from src.date import get_date
from src.generators import card_number_generator, filter_by_description, filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.resources import get_logs
from src.widget import get_mask_card_and_mask_pay

if __name__ == "__main__":

    def mask_card_and_check():
        """
        функция обрабатывающая ввод данных карты/счета, переменная user_card от пользователя запрашивает информацию
        > склеивает все символы и приводит к нижнему регистру
        > из цикла for elem in user_card добавляются данные
        в переменные number_card_or_check и name_card_or_check попадают номер карты и имя держателя карты
        далее идут проверки на совпадение ввода от пользователя
        если все верно то передаем данные в модуль src/widget.py
        если же не прошли проверки, то переменные number_card_or_check и name_card_or_check очищаются
        :return: возвращаем название карты и маскированный номер карты/счета
        """
        # делим строку на название карты/счета и номера карты/счета
        number_card_or_check = ""
        name_card_or_check = ""
        card_names = {
            "visaclassic": "Visa Classic",
            "visaplatinum": "Visa Platinum",
            "visagold": "Visa Gold",
            "visa": "Visa",
            "mastercard": "Mastercard",
            "maestro": "Maestro",
        }

        is_correct_pay = True
        while is_correct_pay:
            print("Карта/счет и номер карты/счета: ", end="")
            user_card = input().replace(" ", "").lower()
            # склеиваем все символы вместе
            for elem in user_card:
                if elem.isdigit():
                    number_card_or_check += elem
                elif elem.isalpha():
                    name_card_or_check += elem
            if len(number_card_or_check) == 16:
                for min_name, full_name in card_names.items():
                    if name_card_or_check.startswith(min_name) and len(number_card_or_check) == 16:
                        name_card_or_check = full_name
                        is_correct_pay = False
                        break
            elif name_card_or_check in ("счет", "счёт") and len(number_card_or_check) == 20:
                name_card_or_check = "счет"
                is_correct_pay = False
            else:
                print("Некорректный номер или карта")
                name_card_or_check = ""
                number_card_or_check = ""
        # если все проверки удачны, передаем данные на обработку
        # счет
        if name_card_or_check.startswith("счет"):
            mask_check = get_mask_card_and_mask_pay(number_card_or_check)
            return f"Счет {mask_check}"
        # карта
        mask_card = get_mask_card_and_mask_pay(number_card_or_check)
        return f"{name_card_or_check} {mask_card}"

    # вызов функции mask_card_and_check()
    mask_pay = mask_card_and_check()
    print(mask_pay)
    # системная дата устройства
    date = get_date()
    print(f"\nТекущая дата {date}\n")

    # логи(id, статус, дата, операция, сумма средств, валюта, перевод от кого(организация счет или карта) и кому
    logs = get_logs()

    # передаем функции в модуле src/processing.py данные из списка словарей для деления на две строки
    # по статусу выполнения операций
    EXECUTED_LOGS = filter_by_state(logs, state="EXECUTED")
    print(f"Журнал задач:\n  по статусу:\n\t{EXECUTED_LOGS}")

    # передаем функции в модуле src/processing.py данные из списка словарей для сортировки по дате и времени операций
    logger_reverse = sort_by_date(logs, sort=True)
    print(f"  по дате:\n\t{logger_reverse}\n")

    # создаем объект генератора, передаем аргумент в функцию в модуле src/generators.py данные из списка словарей(logs)
    identifier = filter_by_currency(logs, "USD")

    # идентификатор операции
    try:
        for _id in range(len(logs)):
            print(next(identifier))
    except StopIteration:
        pass
    finally:
        print()

    # описание операции(транзакций)
    description = filter_by_description(logs)
    try:
        while True:
            print(next(description))
    except StopIteration:
        pass
    finally:
        print()

    # генерация номеров карт
    QUANTITY = 5
    gen_num_card = card_number_generator(QUANTITY, 0, 9)
    for card in range(QUANTITY):
        print(next(gen_num_card))
