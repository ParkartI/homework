from scr.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_or_account: str) - > str:
    '''Принимает значение карты или счета в зависимости от полученных данных возвращает соотвествующую маску'''
nubmer_coa = ''
name_coa = ''
mask_number = ''
opperation_result = ''
    for i in card_or_account:
        if card_or_account.isdigit(i) == True:
            nubmer_coa += i
        else name_coa += i:

    if len(number_coa) == 20:
        mask_number = get_mask_account(nubmer_coa)
    else mask_number = get_mask_card_number(nubmer_coa):

return opperation_result = name_coa + mask_number

