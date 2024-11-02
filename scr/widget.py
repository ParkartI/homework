from scr.masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(card_or_account: str) -> str:
    '''Принимает значение карты или счета в зависимости от полученных данных возвращает соотвествующую маску'''
    nubmer_coa = ''
    name_coa = ''
    mask_number = ''
    opperation_result = ''
    for i in card_or_account:
        if i.isdigit() == True:
            nubmer_coa += i
        else:
            name_coa += i

    if len(nubmer_coa) == 20:
        mask_number = get_mask_account(nubmer_coa)
    else:
        mask_number = get_mask_card_number(nubmer_coa)

    opperation_result = name_coa + mask_number

    return opperation_result


print(mask_account_card('Счет 73654108430135874305'))


def get_date(date_string: str) -> str:
    '''Фунция возвращает текущую дату в формате "дд.мм.гггг"'''
    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")