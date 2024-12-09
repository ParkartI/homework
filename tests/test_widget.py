import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card(input_data: str, expected_data: str) -> str:
    assert mask_account_card(input_data) == expected_data
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("")

    assert str(exc_info.value) == "Введены некорректные данные"


def test_get_date() -> str:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("dsa") == "Неверный формат даты"
