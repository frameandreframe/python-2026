# 2. Built-in generics
# Modern 
from typing import List, Dict

def get_names() -> list[str]:
    return ["Alice", "Bob"]

def get_scores() -> dict[str, int]:
    return {"Alice": 90, "Bob": 85}

def get_numbers() -> List[int]:
    return [1, 2, 3]