# TypeDict
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


if __name__ == "__main__":
    user_data = {"id": 1, "name": "Alice", "email": None}
    user = create_user(user_data)
    print(user, type(user))

    person_data = Person(id=2, name="Bob")
    print(person_data, type(person_data))

    person_data2 = Person(id=2, name="laoban", email="laoban@example.com")
    print(person_data2, type(person_data))



# ===================== 下一件事 =========================

# from pydantic import BaseModel, EmailStr, ValidationError

# class CreateUser(BaseModel):
#     email: EmailStr
#     name: str
#     age: int

# # Coerces compatible types automatically
# user = CreateUser(email="alice@example.com", name="Alice", age="30")
# print(user)
# # CreateUser(email='alice@example.com', name='Alice', age=30)

# # Rejects bad input with structured errors
# try:
#     CreateUser(email="not-an-email", name="Bob", age="not-a-number")
# except ValidationError as e:
#     print(e.json(indent=2))
# # [{"type": "value_error", "loc": ["email"], ...}]