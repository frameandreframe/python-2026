# 5. Protocal
from typing import Protocol, runtime_checkable

@runtime_checkable
class SupportsLen(Protocol):
    """Aprotocol that requoires a __len__ method
    Protocal: 这里只是一个方法声明（signature），没有 body，不要执行
    """

    def __len__(self) -> int: ...  # 只是签名， 没有实现。 类型检查其


def report_size(obj: SupportsLen) -> str:
    """report the size of an object that supports len()"""
    return f"size = {len(obj)}"  #  真正执行时， 调的是自己类型的 __len__


class NoLen:
    """A class that does not implement __len__"""
    pass


class MyBox:
    def __len__(self) -> int:
        return 42



if __name__ == "__main__":
    print(report_size([1, 2, 3])) # OK, list has __len__
    print(report_size("hello")) # Ok, str has __len__
    print(report_size({1: 2})) # Ok, dict has __len__

    print(report_size(MyBox()))
    # print(report_size(NoLen()))
    print(isinstance([1, 2, 3], SupportsLen)) # True
    print(isinstance("hi", SupportsLen))    # True
    print(isinstance(42, SupportsLen))      # False
    print(isinstance(NoLen(), SupportsLen)) # False
    print(isinstance(MyBox(), SupportsLen)) # True