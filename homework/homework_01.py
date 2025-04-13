"""
HOMEWORK1. Fixing syntax errors and various minor tasks.

Task Description:
-----------------
HOMEWORK1 involves the following task.
- Fixing syntax errors.
- Solving small problems to practice declaring variables etc.
- Задачі 07 -10:
Переведіть задачі з книги "Математика, 2 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в другому класі
"""

# task 01 Виправте синтаксичні помилки
# print("Hello", end = " ")
#     print("world!")
# Solution:
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
# hello = "Hello"
# world = "world"
# if True:
# print(f"{hello} {world}!")
# Solution:
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03 Вcтавте пропущену змінну у ф-цію print
# for letter in "Hello world!":
#     print()
# Solution:
for letter in "Hello world!":
    print(letter)

# task 04 Зробіть так, щоб кількість бананів була завжди в чотири рази більша, ніж яблук
# apples = 2
# banana = x
# Solution:
apples = 2
bananas = apples * 4
print(bananas)

# task 05 == виправте назви змінних
# 1_storona = 1
# ?torona_2 = 2
# сторона_3 = 3
# $torona_4 = 4
# Solution:
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# # та виведіть його для користувача
# perimetery = ? + ? + ? + ?
# print()
# Solution:
perimeter = storona_1 + storona_2 + storona_3 + storona_4
print("Perimeter of the figure:", perimeter)

# task 07
# У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
# Скільки всього дерев посадили в саду?
# Solution:
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
total_trees = apple_trees + pear_trees + plum_trees
print("Total trees in the garden:", total_trees)

# task 08
# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?
# Solution:
temperature_morning = 5
temperature_afternoon = temperature_morning - 10
temperature_evening = temperature_afternoon + 4
print("Temperature at evening:", temperature_evening, "degrees")

# task 09
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?
# Solution:
boys = 24
girls = boys // 2
sick_boys = 1
absent_girls = 2
present_boys = boys - sick_boys
present_girls = girls - absent_girls
total_today = present_boys + present_girls
print("Today in the children's circle:", total_today)

# task 10
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
# Solution:
book1 = 8
book2 = book1 + 2
book3 = (book1 + book2) / 2
total_price = book1 + book2 + book3
print("Total cost of all books:", total_price, "uah")
