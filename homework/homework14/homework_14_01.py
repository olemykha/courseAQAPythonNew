"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""


class Student:

    def __init__(self, name: str, surname: str, age: int, gpa: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.gpa = gpa

    def __str__(self) -> str:
        return (f'Student: {self.name} {self.surname} | '
                f'Age: {self.age}, GPA: {self.gpa}')

    def update_gpa(self, new_gpa: float):
        self.gpa = new_gpa
