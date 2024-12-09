import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid() -> str:
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


def test_get_mask_card_number_invalid_non_digit() -> str:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("1234 5678 9012 3456")
    assert str(
        exc_info.value) == "Номер должен состоять из цифр, без пробелов. Количество цифр должно быть равно шестнадцати"


def test_get_mask_card_number_invalid_characters() -> str:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("1234abcd5678901234")
    assert str(
        exc_info.value) == "Номер должен состоять из цифр, без пробелов. Количество цифр должно быть равно шестнадцати"


def test_valid_account_number() -> str:
    account_number = "12345678901234567890"
    expected = "**7890"
    assert get_mask_account(account_number) == expected


def test_invalid_account_number_length_short() -> str:
    account_number = "1234567890123456789"
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_number)
    assert str(
        exc_info.value) == "Номер должен состоять из цифр, без пробелов. Количество цифр должно быть равно двадцати"
