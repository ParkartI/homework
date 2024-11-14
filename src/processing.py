from typing import List, Dict


def filter_by_state(data: dict, state='EXECUTED'): -> dict
    """Функция возвращает словари у которых ключ state соответствует указанному значению"""

    return [entry for entry in data if entry.get('state') == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    return sorted(data, key=lambda x: x['date'], reverse=descending)