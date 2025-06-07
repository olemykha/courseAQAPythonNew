# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    user_input_word = input(f'Enter a word that contains the letter \'h\': ')
    if 'h' in user_input_word.lower():
        print(f'Thank you! Your word: "{user_input_word}" contains the letter \'h\'.')
        break
    else:
        print(f'The word doesn\'t contain the letter \'h\'. Please try again.')
