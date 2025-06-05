import pytest
from homework.homework9.functions import sum_of_two_numbers, average, reverse_string


# Tests for 'sum_of_two_numbers' function

def test_sum_positive_numbers():
    assert sum_of_two_numbers(5, 7) == 12


def test_sum_negative_and_positive():
    assert sum_of_two_numbers(-3, 10) == 7


def test_sum_with_zero():
    assert sum_of_two_numbers(0, 0) == 0


# def test_sum_large_values():
#     assert sum_of_two_numbers(1_000_000, 2_000_000) == 3_000_000


# Tests for 'average' function

def test_average_of_multiple_integers():
    assert average([2, 4, 6, 8]) == 5.0


def test_average_of_single_element():
    assert average([42]) == 42.0


def test_average_empty_list():
    assert average([]) == "Error: the list is empty."


# Tests for 'reverse_string' function

def test_reverse_regular_string():
    assert reverse_string("hello") == "olleh"


def test_reverse_single_character():
    assert reverse_string("A") == "A"


def test_reverse_palindrome():
    assert reverse_string("radar") == "radar"


def test_reverse_empty_string():
    assert reverse_string("") == "Error: the string is empty."
