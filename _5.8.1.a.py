from dataclasses import dataclass
from typing import Union

@dataclass
class Left:
    a: float

@dataclass
class Right:
    b: float

Either = Union[Left, Right]
