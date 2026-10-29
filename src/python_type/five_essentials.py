# Function signatures
def calculate_discount(price: float, percent: int) -> float:
    return price * (1 - percent / 100)


# 2. Built-in generics
# Modern 
def get_names() -> list[str]:
    return ["Alice", "Bob"]

def get_scores() -> dict[str, int]:
    return {"Alice": 90, "Bob": 85}

# Legacy form (still works, but unnecessary import):
from typing import List, Dict
def get_numbers() -> List[int]:
    return [1, 2, 3]


# 3. Union syntax 3.10+
# Modern (PEP 604)
def parse(value: int | str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None

# Legacy form
from typing import Union, Optional
def parse_before(value: Union[int, str]) -> Optional[int]:...


# 4. TypeDict 
from typing import TypedDict

class User(TypedDict):
    """1. Define a TypeDict for user data with required and optional fields
    2. User 是 TypeDict 的子类，表示一个字典类型， 它描述的是 "这个dict 应该长什么样"
    3. User 本质上是一个 "字典的形状生命"(schema), 不是真正的实例化类
    4. 运行时 user 就是普通的 dict, type(user) 打印出来的是 <class 'dict'>, 但是它的类型注解是 User
    5. TypedDict 只服务于静态类型检查器 (mypy, pyright, IDE), 不做运行时校验
    
    """
    id: int
    name: str
    email: str | None # optional value, but key must be present. None表示这个键是必须的


_REQUIRED_KEYS = {"id", "name", "email"}


def create_user(data: User) -> User:
    """create a new datatype with class"""
    missing = _REQUIRED_KEYS - data.keys()
    if missing:
        raise TypeError(f"Missing required keys: {sorted(missing)}")
    return data


from typing import NotRequired # python 3.11+

class Person(TypedDict):
    """person is a TypedDict with optional fields"""
    id: int
    name: str
    email: NotRequired[str | None] # 希望这个键本身可以不存在， 键可以缺省 


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



if __name__ == "__main__":
    discount = calculate_discount(100, 2)
    print(f"Discount: {discount}")

# 
# 
# cd ~/projects/beginers/python_type$ uv run python -c "import python_type.five_essentials;print('ok')"
# 