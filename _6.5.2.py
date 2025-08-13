from dataclasses import dataclass
from typing import Union
from math import pi

@dataclass(frozen=True)
class Circle:
    radius: float

@dataclass(frozen=True)
class Rect:
    width:  float
    height: float

@dataclass(frozen=True)
class Square:
    size: float

Shape = Union[Circle, Rect]

def area (shape: Shape) -> float:
    match shape:
        case Circle(radius):
            return pi * radius**2
        case Rect(width, height):
            return width * height
        case Square(size):
            return size**2
        case _:
            raise TypeError("Unknown shape")

def circ (shape: Shape) -> float:
    match shape:
        case Circle (radius):
            return 2.0 * pi * radius
        case Rect (width, height):
            return 2.0 * (width + height)
        case Square (size):
            return 4.0 * size
        case _:
            raise TypeError("Unknown shape")

def main():
    circle = Circle (2.0)
    print(area(circle))
    print(circ(circle))
