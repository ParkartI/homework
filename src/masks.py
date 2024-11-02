def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает ее зашифрованный вариант"""
    masked_number = card_number[0:4] + " " + card_number[4:6] + "** ****" + " " + card_number[12:16]
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Принимает номер счета и возвращает его зашифрованный вариант"""
    account_str = str(account_number)

    masked_account = "**" + account_str[-4:]

    return masked_account
