def get_mask_card_number(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает его замаскированным"""
    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_account: str) -> str:
    """Функция принимает на вход номер карты и возвращает маску номера счёта."""
    return f"** {number_account[-4:]}"
