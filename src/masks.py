def get_mask_card_number(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает его замаскированным"""
    if len(number_card) == 16:
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"
    return "Некорректный номер"


def get_mask_account(number_account: str) -> str:
    """Функция принимает на вход номер карты и возвращает маску номера счёта."""
    if len(number_account) == 20:
        return f"** {number_account[-4:]}"
    return "Некорректный номер"


# def get_date(data: str) -> str:
#     """Принимает на вход строку и возвращает дату"""
#     if data=='':
#             return ''
#     return f"{data[8:10]}.{data[5:7]}.{data[:4]}"
