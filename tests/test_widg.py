import pytest

from src.widg import funk, get_date


def test_get_date(get_data):
    """Тест функции get_date"""
    assert get_date("2024-03-11T02:26:18.671407") == get_data


@pytest.mark.parametrize(
    "date, targ",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02:26:18.6123", "11.03.2024"),
        ("", ""),
        ("2023-04-11T02:26:18.6123", "11.04.2023"),
    ],
)
def test_get_date_param(date, targ):
    """Тест функции get_date"""
    assert get_date(date) == targ


@pytest.mark.parametrize(
    "inf_the_card, mask",
    [
        ("Visa Platinum 1234567890123456", " Visa Platinum 1234 56** **** 3456"),
        ("Maestro 9876543210123456", " Maestro 9876 54** **** 3456"),
        ("Счет 1234567890123456790", "Некорректный номер счёта"),
        ("Счет 12345678901234567890", "Счет ** 7890"),
    ],
)
def test_mask_account_card(inf_the_card: str, mask: str) -> str:
    """Тест функции funk"""
    assert funk(inf_the_card) == mask
