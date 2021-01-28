from datetime import datetime
from typing import Union


EPOCH = datetime.utcfromtimestamp(0)


def date2microseconds(date: datetime) -> int:
    return int((date - EPOCH).total_seconds() * 1000000.0)


def microseconds2date(microseconds: float) -> datetime:
    return datetime.utcfromtimestamp(microseconds / 1000000)


def try_parse_float(x: Union[str, float, int]) -> Union[float, str]:
    try:
        return float(x)
    except ValueError:
        return x
