from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Принимает значение карты или счета в зависимости от полученных данных возвращает соотвествующую маску"""
    nubmer_coa = ""
    name_coa = ""
    mask_number = ""
    opperation_result = ""
    space_counter = -1

    for i in card_or_account:
        if i.isdigit():
            nubmer_coa += i
        else:
            name_coa += i

    if len(nubmer_coa) == 20:
        mask_number = get_mask_account(nubmer_coa)
    else:
        mask_number = get_mask_card_number(nubmer_coa)

    while name_coa[space_counter] == " ":
        name_coa = name_coa[: len(name_coa) - 1]

    name_coa += " "

    opperation_result = name_coa + mask_number

    return opperation_result


def get_date(date_string: str) -> str:
    """Фунция возвращает текущую дату в формате "дд.мм.гггг" """

    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")
