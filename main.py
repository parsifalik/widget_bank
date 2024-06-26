"""программа для скрытия номера карты/счета"""

from src.date import get_date
from src.processing import filter_by_state, sort_by_date
from src.widget import get_mask_card_and_mask_pay
from src.generators import filter_by_identifier, filter_by_description, card_number_generator
from src.resources import get_logs

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

            card_names = ["maestro", "mastercard", "visaclassic", "visaplatinum", "visagold", "visa"]
            if (any(name_card_or_check.startswith(pay) for pay in card_names)) and (len(number_card_or_check) == 16):
                if (name_card_or_check[:4] == "visa") and (name_card_or_check[4:11] == "classic"):
                    name_card_or_check = "Visa Classic"
                elif (name_card_or_check[:4] == "visa") and (name_card_or_check[4:12]) == "platinum":
                    name_card_or_check = "Visa Platinum"
                elif (name_card_or_check[:4] == "visa") and (name_card_or_check[4:8] == "gold"):
                    name_card_or_check = "Visa Gold"
                elif name_card_or_check == "visa":
                    name_card_or_check = "Visa"
                elif name_card_or_check == "mastercard":
                    name_card_or_check = "Mastercard"
                elif name_card_or_check == "maestro":
                    name_card_or_check = "Maestro"
                is_correct_pay = False
            elif (name_card_or_check == "счет" or name_card_or_check == "счёт") and len(number_card_or_check) == 20:
                name_card_or_check = "счет"
                is_correct_pay = False
            else:
                print("Некорректный номер или карта")
                name_card_or_check = ""
                number_card_or_check = ""

        """Вызов и передача функции номера карты пользователя"""
        # если все проверки удачны, передаем данные на обработку маскировки карты/счета
        if name_card_or_check.startswith("счет"):
            mask_check = get_mask_card_and_mask_pay(number_card_or_check)
            return f"Счет {mask_check}"
        else:
            mask_card = get_mask_card_and_mask_pay(number_card_or_check)
            return f"{name_card_or_check} {mask_card}"

    # вызов функции mask_card_and_check()
    mask_pay = mask_card_and_check()
    print(mask_pay)

    # системная дата устройства
    date = get_date()
    print(f"\nТекущая дата {date}\n")

    # логи(id, статус, дата, операция, сумма средств, валюта, перевод от кого(организация счет или карта) и кому перевод
    logs = get_logs()

    # передаем функции в модуле src/processing.py данные из списка словарей для деления на две строки
    # по статусу выполнения операций
    logger = filter_by_state(logs, state="EXECUTED")
    print(f"Журнал задач:\n  по статусу:\n\t{logger}")

    # передаем функции в модуле src/processing.py данные из списка словарей для сортировки по дате и времени операций
    logger_reverse = sort_by_date(logs, sort=True)
    print(f'  по дате:\n\t{logger_reverse}\n')

    """
    создаем объект генератора, передаем аргумент в функцию в модуле src/generators.py данные из списка словарей(logs) 
    для вывода идентификатора операции/описание операций(транзакций)/генерация номеров карт
    """
    # идентификатор операции
    identifier = filter_by_identifier(logs, "USD")

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

    #генерация номеров карт
    quantity = 5
    gen_num_card = card_number_generator(quantity, 0, 9)
    for card in range(quantity):
        print(next(gen_num_card))
