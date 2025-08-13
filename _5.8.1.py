from dataclasses import dataclass
from typing import Generic, TypeVar

L = TypeVar("L")
R = TypeVar("R")

@dataclass
class Left:
    a: L

@dataclass
class Right:
    b: R

@dataclass
class Either(Generic[L,R]):
    pass

def safe_div(x: float, y: float) -> Either[str, float]:
    if y == 0:
        return Left("Division by zero")
    return Right(x/y)
