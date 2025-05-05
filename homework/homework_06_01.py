# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

user_input = input("Enter your message here: ")
unique_chars = set(user_input)

if len(unique_chars) > 10:
    print(True)
else:
    print(False)
