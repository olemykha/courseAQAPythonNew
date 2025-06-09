"""
Створіть клас геометричної фігури "Ромб".
Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.
"""


class Rhombus:

    def __init__(self, side_a: float, angle_a: float):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                raise ValueError("The side_a must be > 0.")
            super().__setattr__(key, value)

        elif key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("The angle_a must be between 0 and 180")
            super().__setattr__("angle_a", value)
            super().__setattr__("angle_b", 180 - value)

        elif key == "angle_b":
            raise AttributeError("Not allowed. Please, specify value for angle_a instead.")

        else:
            super().__setattr__(key, value)

    def __str__(self):
        return (
            f'Rhombus(side_a={self.side_a} length, '
            f'angle_a={self.angle_a} deg, angle_b={self.angle_b} deg)'
        )
