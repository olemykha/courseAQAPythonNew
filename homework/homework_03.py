"""
HOMEWORK3.
Task Description:
-----------------
HOMEWORK3 involves the following task:
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 Виведіть змінну alice_in_wonderland на друк

# Задачі 04 -10:
# Переведіть задачі з книги "Математика, 5 клас"
# на мову пітон і виведіть відповідь, так, щоб було
# зрозуміло дитині, що навчається в п'ятому класі

# task 04
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?

# task 05
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.

# task 06
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.

# task 07
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9


# task 08
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн

# task 09
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?


# task 10
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

from decimal import Decimal

SEPARATOR = '-' * 77  # Just a separator for readability in the console.

# Solutions:
# Task 1-3
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

print(alice_in_wonderland)

print(SEPARATOR)
# Task 4
black_sea_area = 436_402
azov_sea_area = 37_800

total_area = black_sea_area + azov_sea_area

print(f'Total area of both seas (black and azov) = {total_area} km²')

print(SEPARATOR)
# Task 5
total_items_in_3_storages = 375_291
items_in_1_and_2_storages = 250_449
items_in_2_and_3_storages = 222_950

items_in_storage_1 = total_items_in_3_storages - items_in_2_and_3_storages
items_in_storage_2 = items_in_1_and_2_storages - items_in_storage_1
items_in_storage_3 = total_items_in_3_storages - (items_in_storage_1 + items_in_storage_2)

print(f'Storage 1: {items_in_storage_1} items')
print(f'Storage 2: {items_in_storage_2} items')
print(f'Storage 3: {items_in_storage_3} items')

print(SEPARATOR)
# Task 6
payment_term_months = 18
monthly_payment = Decimal("1179.00")

total_computer_price = payment_term_months * monthly_payment

print(f'Total cost of the computer: {total_computer_price} UAH')

print(SEPARATOR)
# Task 7
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f'a. 8019 % 8 = {a}')
print(f'b. 9907 % 9 = {b}')
print(f'c. 2789 % 5 = {c}')
print(f'd. 7248 % 6 = {d}')
print(f'e. 7128 % 5 = {e}')
print(f'f. 19224 % 9 = {f}')

print(SEPARATOR)
# Task 8
big_pizza_price = Decimal("274.00")
big_pizza_quantity = 4

medium_pizza_price = Decimal("218.00")
medium_pizza_quantity = 2

juice_price = Decimal("35.00")
juice_quantity = 4

cake_price = Decimal("350.00")
cake_quantity = 1

water_price = Decimal("21.00")
water_quantity = 3

total_sum = (
    big_pizza_quantity * big_pizza_price +
    medium_pizza_quantity * medium_pizza_price +
    juice_quantity * juice_price +
    cake_quantity * cake_price +
    water_quantity * water_price
)

print(f'Total cost of order = {total_sum} UAH')

print(SEPARATOR)
# Task 9
all_igors_photo = 232
photo_capacity_for_one_page = 8

pages_needed = 232 // 8

print(pages_needed)

print(SEPARATOR)
# Task 10
distance_from_kh_to_bdp = 1600
fuel_consumption_per_100_km = 9
tank_capacity = 48

fuel_needed = (distance_from_kh_to_bdp / 100) * fuel_consumption_per_100_km
number_of_fuel_fills = fuel_needed // tank_capacity

print(f'Fuel needed for the trip: {fuel_needed} liters')
print(f'Number of refuels needed: {number_of_fuel_fills}')
