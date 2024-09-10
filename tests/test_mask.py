import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state
from src.widg import funk, get_date


@pytest.mark.parametrize(
    "number_card, mask",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210123456", "9876 54** **** 3456"),
        ("", "Некорректный номер"),
        ("-12345678912345", "Некорректный номер"),
    ],
)
def test_get_mask_card_number(number_card, mask):
    """Тест функции get_mask_card_number"""
    assert get_mask_card_number(number_card) == mask


@pytest.mark.parametrize(
    "number_account, mask",
    [("12345678901234567890", "** 7890"), ("98765432109876543210", "** 3210"), ("", "Некорректный номер")],
)
def test_get_mask_account(number_account, mask):
    """Тест функции get_mask_account"""
    assert get_mask_account(number_account) == mask


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


def test_get_mask_card(get_mask):
    """Тест функции get_mask_card_number"""
    assert get_mask_card_number("1234567890123456") == get_mask


@pytest.mark.parametrize(
    "list_dictionaries, state",
    [
        (
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
        ),
        ([{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], []),
        ([], []),
    ],
)
def test_filter_by_state(list_dictionaries, state):
    """Тест функции filter_by_state"""
    assert filter_by_state(list_dictionaries) == state


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
