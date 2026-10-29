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