# Tier 2: Worth Knowing

# 1. NewType for distinct identifiers
from typing import NewType

UserId = NewType('UserId', int)
OrderId = NewType('OrderId', int)

def get_user(uid: UserId) -> None: ...


from typing import TypeVar

T = TypeVar('T')

def first(items: list[T]) -> T:
    """Return the first item from a list of items."""
    return items[0]


if __name__ == "__main__":
    # uid = UserId(42)
    # oid = OrderId(99)

    # print(get_user(uid)) # Ok
    # print(get_user(oid)) # mypy error: incompltible type
    # print(get_user(42))  # mypy error: incompltible type

    # from typing import NewType
    # UserId = NewType('UserId', int)

    # uid = UserId(42)
    # print(uid)                 # 42
    # print(type(uid))           # <class 'int'>      ← 就是 int！
    # print(uid is 42)           # True（CPython 小整数缓存）
    # print(UserId.__name__)     # 'UserId'（有名字，但仅作标记）
    # print(UserId.__supertype__)# <class 'int'>

    # Type checker infers T:
    x: int = first([1, 2, 3])         # T = int, OK
    y: str = first(["a", "b"])         # T = str, OK
    z: int = first(["a", "b"])         # error: T = str, not int