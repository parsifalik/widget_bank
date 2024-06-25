"""программа для скрытия номера карты/счета"""

from src.date import get_date
from src.processing import filter_by_state, sort_by_date
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
        # если все проверки удачны, передаем данные на обработку маскировеи карты/счета
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

    # журнал задач или лог выполненных задач
    list_dict = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    # передаем функции в модуле src/processing.py данные из списка словарей для деления на две строки
    # по статусу выполнения операций
    logger = filter_by_state(list_dict, state="EXECUTED")
    print(f"Журнал задач:\n  по статусу:\n\t{logger}")
    # передаем функции в модуле src/processing.py данные из списка словарей для сортировки по дате и времени операций
    logger_reverse = sort_by_date(list_dict, sort=True)
    print(f'  по дате:\n\t{logger_reverse}')
