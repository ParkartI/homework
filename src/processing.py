from datetime import datetime
from typing import Dict, List


def filter_by_state(data: List[Dict], state="EXECUTED") -> List[Dict]:
    """Функция возвращает список словарей, у которых ключ 'state' соответствует указанному значению"""
    return [entry for entry in data if entry.get("state") == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """Сортирует список словарей по ключу 'date'"""
    return sorted(data, key=lambda x: x["date"], reverse=descending)
