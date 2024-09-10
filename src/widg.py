from src.masks import get_mask_account, get_mask_card_number


def funk(inf_the_card: str) -> str:
    """Принимает тип и номер карты или счёта, возвращает тип и замаскированный номер карты или счёта"""

    if "Счет" in inf_the_card:
        if len(inf_the_card.split()[-1]) == 20:
            return f"{inf_the_card.split()[0]} {get_mask_account(inf_the_card.split()[-1])}"
        else:
            return "Некорректный номер счёта"
    else:
        if len(inf_the_card.split()[-1]) == 16:
            return f" {' ' .join(inf_the_card.split()[0:-1])} {get_mask_card_number(inf_the_card.split()[-1])}"
        else:
            exit("Некорректный номер карты")


def get_date(data: str) -> str:
    """Принимает на вход строку и возвращает дату"""
    if data == "":
        return ""
    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"


a = funk("Счет 1234567890123456790")
print(a)
