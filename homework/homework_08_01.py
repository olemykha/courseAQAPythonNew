"""
HOMEWORK8.

Task Description:
-----------------
HOMEWORK8 involves the following task.

Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
- Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
- Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі),
вам потрібно зловити вийняток і вивести “Не можу це зробити!”
- Використовуйте блок try|except, щоб уникнути інших символів, окрім чисел у списку.
- Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”
"""


def calculate_sum_of_numbers_in_array(array_list: list) -> list:
    result = []

    for item_list in array_list:
        try:
            split_numbers = item_list.split(',')
            counter_for_adding_numbers = 0
            for number in split_numbers:
                counter_for_adding_numbers += int(number)
            result.append(counter_for_adding_numbers)
        except ValueError:
            result.append(f'I can\'t do it')

    return result


test_data = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
print(calculate_sum_of_numbers_in_array(test_data))
