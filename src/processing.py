from typing import List, Dict


def filter_by_state(data: dict, state: str ='EXECUTED') -> list:
    """Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    return [entry for entry in data if entry.get('state') == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """Возвращаtn новый список, отсортированный по дате"""
    return sorted(data, key=lambda x: x['date'], reverse=descending)
