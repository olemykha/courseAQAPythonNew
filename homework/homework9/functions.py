"""Написати функцію, яка обчислює суму двох чисел."""


def sum_of_two_numbers(number1: int, number2: int):
    return number1 + number2


"""Написати функцію, яка розрахує середнє арифметичне списку чисел."""


def average(numbers):
    if not numbers:
        return f'Error: the list is empty.'
    return sum(numbers) / len(numbers)


"""Написати функцію, яка приймає рядок та повертає його у зворотному порядку."""


def reverse_string(some_string: str) -> str:
    if not some_string:
        return f'Error: the string is empty.'
    return some_string[::-1]
