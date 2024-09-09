list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(my_list: list, state_targe="EXECUTED") -> list:
    """Функция которая принимает список словарей и опционально значение для ключа state"""
    list_targe = []
    for key in my_list:
        if key.get("state") == state_targe:
            list_targe.append(key)
    return list_targe


def sort_by_date(my_list: list, reverse=True) -> list:
    """Принимает список словарей и возвращает отсортированный список по убыванию даты"""
    sort_date_list = sorted(my_list, key=lambda date: date.get("date"), reverse=True)
    return sort_date_list


print(filter_by_state(list))
