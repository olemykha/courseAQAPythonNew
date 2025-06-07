# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити/доповнити.
"""


def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            break
        print(f'{number}x{multiplier}={result}')
        multiplier += 1


# task 2
"""Написати функцію, яка обчислює суму двох чисел."""


def sum_of_two_numbers(number1: int, number2: int):
    return number1 + number2


# task 3
"""Написати функцію, яка розрахує середнє арифметичне списку чисел."""


def average(numbers):
    if not numbers:
        return f'Error: the list is empty.'
    return sum(numbers) / len(numbers)


# task 4
"""Написати функцію, яка приймає рядок та повертає його у зворотному порядку."""


def reverse_string(some_string: str) -> str:
    if not some_string:
        return f'Error: the string is empty.'
    return some_string[::-1]


# task 5
"""Написати функцію, яка приймає список слів та повертає найдовше слово у списку."""


def longest_word(list_of_words: list):
    if not list_of_words:
        return 'Error: the list is empty.'

    longest_w = list_of_words[0]
    for word in list_of_words:
        if len(word) > len(longest_w):
            longest_w = word
    return longest_w


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

# def find_substring(str1, str2):
#     return -1
#
#
# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2))  # поверне 7
#
# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# print(find_substring(str1, str2))  # поверне -1


def find_substring(main_string: str, sub_string: str) -> int:
    return main_string.find(sub_string)


# task 7, 8, 9, 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

# user_input = input("Enter your message here: ")
# unique_chars = set(user_input)
#
# if len(unique_chars) > 10:
#     print(True)
# else:
#     print(False)


def has_more_than_10_unique_chars() -> bool:
    """
    The user to input a string and checks if it has more than 10 unique characters.
    Returns:
        True if the string has more than 10 unique chars otherwise False.
    """
    user_input = input("Enter your message here: ")
    unique_chars = set(user_input)

    if len(unique_chars) > 10:
        return True
    else:
        return False


# task 8
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

# while True:
#     user_input_word = input(f'Enter a word that contains the letter \'h\': ')
#     if 'h' in user_input_word.lower():
#         print(f'Thank you! Your word: "{user_input_word}" contains the letter \'h\'.')
#         break
#     else:
#         print(f'The word doesn\'t contain the letter \'h\'. Please try again.')

def input_word_with_h() -> str:
    """
    The user to input a word containing the letter 'h'
    The function ends when a valid word is entered.

    Returns:
        The valid word entered by the user containing the letter 'h'.
    """
    while True:
        user_input_word = input(f'Enter a word that contains the letter \'h\': ')
        if 'h' in user_input_word.lower():
            return f'Thank you! Your word: "{user_input_word}" contains the letter \'h\'.'
        else:
            return f'The word doesn\'t contain the letter \'h\'. Please try again.'


# task 9
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
#
# lst2 = []
#
# for str_item in lst1:
#     if isinstance(str_item, str):
#         lst2.append(str_item)
#
# print(lst2)


def extract_strings_from_list(user_list_of_data: list) -> list:
    """
    Extracts all string elements from a mixed-type list.
    Args:
        user_list_of_data (list): The list that may contain elements of different types.
    Returns:
        lst2: A list containing only the string elements.
    """

    lst2 = []

    for str_item in user_list_of_data:
        if isinstance(str_item, str):
            lst2.append(str_item)

    return lst2


# task 10
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

# list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# sum_of_even_numbers = 0
#
# for number in list_of_numbers:
#     if number % 2 == 0:
#         sum_of_even_numbers += number
#
# print(f"Sum of all even numbers = {sum_of_even_numbers}")

def sum_of_even_numbers(list_of_numbers: list):
    """
    Calculates the sum of all even numbers in the provided list.
    Args:
        list_of_numbers (list): A list of integers.
    Returns:
        The sum of all even numbers into fstring.
    """

    sum_of_even_numbs = 0
    for number in list_of_numbers:
        if number % 2 == 0:
            sum_of_even_numbs += number

    return f"Sum of all even numbers = {sum_of_even_numbs}"
