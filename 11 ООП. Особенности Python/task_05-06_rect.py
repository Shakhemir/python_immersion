"""
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
Задание №6.
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""


class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if b is None else b

    def get_perimeter(self):
        return (self.a + self.b) * 2

    def get_square(self):
        return self.a * self.b

    def __add__(self, other):
        return Rectangle(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Rectangle(abs(self.a - other.a), abs(self.b - other.b))

    def __str__(self):
        return f'({self.a}, {self.b})'

    def __repr__(self):
        return f'Rectangle({self.a}, {self.b}), perimeter = {self.get_perimeter()}, square = {self.get_square()}'

    def __eq__(self, other):
        return self.get_perimeter() == other.get_perimeter()

    def __gt__(self, other):
        return self.get_perimeter() > other.get_perimeter()

    def __ge__(self, other):
        return self.get_perimeter() >= other.get_perimeter()


if __name__ == '__main__':
    rect1 = Rectangle(5, 3)
    print(f'{rect1 = }')
    rect2 = Rectangle(15, 2)
    print(f'{rect2 = }')
    rect3 = rect1 + rect2
    print(f'{rect1 + rect2 = }')
    rect4 = rect2 - rect1
    print(f'{rect2 - rect1 = }')
    print(f'{rect1 <= rect2 = }')

