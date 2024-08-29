from masks import get_mask_account, get_mask_card_number
from datetime import date

if __name__ == "__main__":

    def mask_account_card(inf_the_card: str) -> str:
        """Принимает тип и номер карты или счёта, возвращает тип и замаскированный номер карты или счёта"""

        if "Счет" in inf_the_card:
            if len(inf_the_card.split()[-1]) == 20:
                return f"{inf_the_card.split()[0]} { get_mask_account(inf_the_card.split()[-1])}"
            else:
                exit("Некорректный номер счёта")
        else:
            if len(inf_the_card.split()[-1]) == 16:
                return f" {' ' .join(inf_the_card.split()[0:-1])} {get_mask_card_number(inf_the_card.split()[-1])}"
            else:
                exit("Некорректный номер карты")

    def get_date(data: str) -> str:
        """Принимает на вход строку и возвращает дату"""
        return f"{data[8:10]}.{data[5:7]}.{data[:4]}"


print("Введите 'Visa Platinum' или 'Maestro' или 'Счет' и номер вашей карты или счета")
inf_the_card = input()

data = mask_account_card(inf_the_card)
ddmmyyyy = get_date("2024-03-11T02:26:18.671407")

print(data)
print(ddmmyyyy)
