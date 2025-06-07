# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_of_even_numbers = 0

for number in list_of_numbers:
    if number % 2 == 0:
        sum_of_even_numbers += number

print(f"Sum of all even numbers = {sum_of_even_numbers}")
