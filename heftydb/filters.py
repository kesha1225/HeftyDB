import typing
import re

from ._types import HeftyObject


def greater_than(obj: HeftyObject, check_key: str, filter_value: typing.Any) -> bool:
    return obj[check_key] > filter_value


def less_than(obj: HeftyObject, check_key: str, filter_value: typing.Any) -> bool:
    return obj[check_key] < filter_value


def greater_than_equal(
    obj: HeftyObject, check_key: str, filter_value: typing.Any
) -> bool:
    return obj[check_key] >= filter_value


def less_than_equal(obj: HeftyObject, check_key: str, filter_value: typing.Any) -> bool:
    return obj[check_key] <= filter_value


def in_(obj: HeftyObject, check_key: str, filter_value: typing.Any) -> bool:
    return obj[check_key] in filter_value


def contains(obj: HeftyObject, check_key: str, filter_value: typing.Any) -> bool:
    return filter_value in obj[check_key]


def icontains(obj: HeftyObject, check_key: str, filter_value: typing.Any) -> bool:
    return filter_value not in obj[check_key]


def iexact(obj: HeftyObject, check_key: str, filter_value: str) -> bool:
    return filter_value.lower() == obj[check_key].lower()


def regex(obj: HeftyObject, check_key: str, filter_value: str, flags: int = 0) -> bool:
    pattern = re.compile(filter_value, flags)
    return pattern.match(obj[check_key]) is not None


def iregex(obj: HeftyObject, check_key: str, filter_value: str, flags: int = 0) -> bool:
    pattern = re.compile(filter_value, flags)
    return pattern.match(obj[check_key]) is None


# todo: range

HEFTY_FILTERS: typing.Dict[
    str, typing.Callable[[HeftyObject, str, typing.Any], bool]
] = {
    "gt": greater_than,
    "lt": less_than,
    "gte": greater_than_equal,
    "lte": less_than_equal,
    "in": in_,
    "contains": contains,
    "icontains": icontains,
    "iexact": iexact,
    "regex": regex,
    "iregex": iregex,
}
