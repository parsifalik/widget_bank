<i>
# Программа для скрытия номера карты или счета
Эта программа написана на языке Python и предоставляет 
возможность пользователю скрыть номера карт и счетов, 
а также ведет логирование времени последних операций.
- карты которые принимает программа:

1)    Maestro 1596837868705199
2)    MasterCard 7158300734726758
3)    Visa Classic 6831982476737658
4)    Visa Platinum 8990922113665229
5)    Visa Gold 5999414228426353
6)    Visa 6131682476437698
7)    Счет 64686473678894779589

## Установка:
1) Клонируйте репозиторий:

git clone https://github.com/parsifalik/widget_bank.git

2) Установите зависимости:

`pip install -r requirements.txt`

## Использование

Запустите программу, введите номер карты или счета, 
и программа скроет часть номера, отображая только маскированные данные.

`python main.py`

    Пример вывода:
    
    Карта/счет и номер карты/счета: visa 8888 8888 8888 8888
    Visa 8888 88** **** 8888
    
    Текущая дата 26.06.24
    
    Журнал задач:
      по статусу:
        [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}]
        [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}]
      по дате:
        [{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}]
    
    939719570
    142264268
    895315941
    
    Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
    
    1810 7415 0244 8277
    2028 0656 9686 1639
    5036 5066 6431 9789
    5261 2068 8009 4481
    1375 5390 8622 7693

## Модули

    date.py
        Модуль date.py содержит функцию get_date(), 
        которая возвращает системную дату устройства в формате день.месяц.год.

---

    widget.py
    
        Содержит функцию get_mask_card_and_mask_pay(card_and_pay), 
        которая принимает номер карты или счета и возвращает маскированные данные.
---

    processing.py
    
        Содержит функции для фильтрации и сортировки логов операций:
    
            filter_by_state(list_dict, state): Фильтрует логи по статусу выполнения операций ("EXECUTED" или "CANCELED").
    
            sort_by_date(list_dict, sort): Сортирует логи по дате операций в порядке возрастания или убывания.
---

    resourses.py
        
        содержит логи(список словарей)
---

    generators.py

        содержит генераторы на вывод в консоль id операции, описание операции(от кого и кому), генерация карт длиной 
        в 16 символов
## Тестирование
Тесты для программы находятся в пакете `tests` и включают следующие проверки:

- Проверка функции скрытия номера карты или счета `test_widget.py`.
- Проверка фильтрации логов по статусу и дате`test_processing.py`.
- Проверка функции получения системной даты `test_date.py`
- в conftest находятся фикстуры для модуля processing
<h3>`test_generators`</h3>
  - Проверка на генерацию карт
  - Проверка на id операции
  - Проверка на корректный возврат описание операции(от кого и кому)

Для запуска тестов используйте:
`pytest`
</i>