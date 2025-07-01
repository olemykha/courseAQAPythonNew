import math
import pytest

from homework.homework16.task2.geometry import Rectangle, Circle, Triangle, Figure


def test_cannot_instantiate_abstract_figure():
    with pytest.raises(TypeError):
        Figure()


@pytest.mark.parametrize(
    "width, height, expected_area, expected_perimeter",
    [
        (4, 5, 20, 18),
        (1.5, 2.5, 3.75, 8.0),
        (10, 10, 100, 40),
    ],
)
def test_rectangle(width, height, expected_area, expected_perimeter):
    rect = Rectangle(width, height)
    assert rect.area() == pytest.approx(expected_area)
    assert rect.perimeter() == pytest.approx(expected_perimeter)


@pytest.mark.parametrize(
    "radius, expected_area, expected_perimeter",
    [
        (1, math.pi * 1**2, 2 * math.pi * 1),
        (2.5, math.pi * 2.5**2, 2 * math.pi * 2.5),
    ],
)
def test_circle(radius, expected_area, expected_perimeter):
    c = Circle(radius)
    assert c.area() == pytest.approx(expected_area)
    assert c.perimeter() == pytest.approx(expected_perimeter)


@pytest.mark.parametrize(
    "a, b, c, expected_area, expected_perimeter",
    [
        (3, 4, 5, 6, 12),
        (5, 5, 6, 12.0, 16.0),
        (2.5, 3.5, 4.5, None, 10.5),
    ],
)
def test_triangle(a, b, c, expected_area, expected_perimeter):
    tri = Triangle(a, b, c)
    assert tri.perimeter() == pytest.approx(expected_perimeter)
    s = (a + b + c) / 2
    true_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    assert tri.area() == pytest.approx(true_area)


def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 10).area()
