from typing import Callable, TypeVar

A = TypeVar ("A")
B = TypeVar ("B")
R = TypeVar ("R")

def fmap (f: Callable [[A], B], g: Callable [[R], A]) -> Callable [[R], B]:
    return lambda r: f(g(r))

def g(env: dict) -> int:
    return env["x"]

def f(n: int) -> str:
    return f"Value is {n}"

h = fmap(f, g)

result = h({"x": 42})
print (result)
# $ python ./ch7.4.3.py 
# $ Value is 42
