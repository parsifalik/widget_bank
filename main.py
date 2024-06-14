"""программа для скрытия номера карты/счета"""
from src.widget import get_mask_card_and_mask_pay
from src.date import get_date

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
