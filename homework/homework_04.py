"""
HOMEWORK4.

Task Description:
-----------------
HOMEWORK4 involves the following task:
ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
task 01
Дані у строці adventures_of_tom_sawyer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")

task 02
Замініть .... на пробіл

task 03
Зробіть так, щоб у тексті було не більше одного пробілу між словами.

task 04
Виведіть, скількі разів у тексті зустрічається літера "h"

task 05
Виведіть, скільки слів у тексті починається з Великої літери?

task 06
Виведіть позицію, на якій слово Tom зустрічається вдруге

task 07
Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
adwentures_of_tom_sawer_sentences = None

task 08
Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.

task 09
Перевірте чи починається якесь речення з "By the time".

task 10
Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.

"""

SEPARATOR = '-' * 77  # Just a separator for readability in the console.

adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# Solutions:

# Task 1
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("\n", " ")

print(adventures_of_tom_sawyer)

# Task 2
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("....", " ")

print(adventures_of_tom_sawyer)

# Task 3
adventures_of_tom_sawyer = " ".join(adventures_of_tom_sawyer.split())

print(adventures_of_tom_sawyer)

# Task 4
count_h = adventures_of_tom_sawyer.count("h")

print(f'The letter "h" appears {count_h} times in the text.')

# Task 5
words = adventures_of_tom_sawyer.split()
capitalized_words = 0

for word in words:
    if word[0].isupper():
        capitalized_words += 1

print(f'Number of words starting with a capital letter = {capitalized_words}')

# Task 6
first_index = adventures_of_tom_sawyer.find("Tom")
second_index = adventures_of_tom_sawyer.find("Tom", first_index + 1)

print(f'The second "Tom" appears at character index: {second_index}')

# Task 7
adventures_of_tom_sawyer_sentences = []

for sentence in adventures_of_tom_sawyer.split("."):
    cleaned = sentence.strip()
    if cleaned:
        adventures_of_tom_sawyer_sentences.append(cleaned + ".")

print(adventures_of_tom_sawyer_sentences)

# Task 8
adventures_of_tom_sawyer_sentences_4_sen = adventures_of_tom_sawyer_sentences[3].lower()

print(f'The fourth sentence is in lowercase : {adventures_of_tom_sawyer_sentences_4_sen}')

# Task 9
for sentence in adventures_of_tom_sawyer_sentences:
    if sentence.startswith("By the time"):
        print('Found a sentence starting with "By the time" : ' + sentence)
        break
else:
    print('No sentence starts with "By the time".')

# Task 10
last_sentence = adventures_of_tom_sawyer_sentences[-1]
word_count = len(last_sentence)

print(f'Number of words in the last sentence = {word_count}')
