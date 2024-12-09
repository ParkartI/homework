def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает ее зашифрованный вариант"""
    if len(card_number) == 16 and card_number.isdigit() == True:
        masked_number = card_number[0:4] + " " + card_number[4:6] + "** ****" + " " + card_number[12:16]
    else:
        raise ValueError("Номер должен состоять из цифр, без пробелов. Количество цифр должно быть равно шестнадцати")
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Принимает номер счета и возвращает его зашифрованный вариант"""
    if len(account_number) == 20 and account_number.isdigit() == True:
        account_str = str(account_number)
        masked_account = "**" + account_str[-4:]
    else:
        raise ValueError("Номер должен состоять из цифр, без пробелов. Количество цифр должно быть равно двадцати")

    return masked_account
