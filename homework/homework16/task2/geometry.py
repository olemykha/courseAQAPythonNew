from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Figure):

    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)


class Circle(Figure):

    def __init__(self, radius: float):
        self._radius = radius

    def area(self) -> float:
        return math.pi * self._radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius


class Triangle(Figure):

    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    def area(self) -> float:
        s = (self._a + self._b + self._c) / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    def perimeter(self) -> float:
        return self._a + self._b + self._c
