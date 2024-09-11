import pytest

from src.masks import get_mask_account, get_mask_card_number


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


def test_get_mask_card(get_mask):
    """Тест функции get_mask_card_number"""
    assert get_mask_card_number("1234567890123456") == get_mask
