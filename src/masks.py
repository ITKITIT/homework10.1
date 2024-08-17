
def get_mask_card_number(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает его замаскированным."""
    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_account: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его замаскированным."""
    return f'** {number_account[-4:]}'

if __name__=='__main__':
  print("Введите номер карты 16 цифр без пробела или номер счёта 20 цифр без пробела")
  number = input()

if len(number) < 16:
    print("Ошибка введите корректный номер карты или номер счёта")
elif len(number) == 16:
    number_card = number
    print("Номер карты принят")
    mask_number = get_mask_card_number(number_card)
    print(mask_number)
elif len(number) == 20:
    number_account = number
    print("Номер счёта принят")
    mask_account = get_mask_account(number_account)
    print(mask_account)


