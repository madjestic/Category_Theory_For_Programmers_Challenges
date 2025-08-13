from dataclasses import dataclass
from typing import Generic, TypeVar, Union

L = TypeVar("L")
R = TypeVar("R")

@dataclass(frozen=True)
class Left(Generic[L,R]):
    value: L

@dataclass(frozen=True)
class Right(Generic[L,R]):
    value: R

Either = Union[Left [L,R], Right[L,R]]

def safe_div(x: float, y: float) -> Either[str, float]:
    if y == 0:
        return Left("Division by zero")
    return Right(x/y)
