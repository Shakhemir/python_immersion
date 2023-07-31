"""
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Fish(Animal):
    def __init__(self, name, age, tail_length):
        super().__init__(name, age)
        self.tail_length = tail_length

    def get_age(self):
        return f'{self.age} лет'


class Bird(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def get_speed(self):
        return f'{self.speed} км/ч'


class Horse(Animal):
    def __init__(self, name, age, power):
        super().__init__(name, age)
        self.power = power

    def get_name(self):
        return f'Крассавчик {super().get_name()}'


if __name__ == '__main__':
    horse = Horse('Черный', 13, 'ииииииггггоооо')
    print(horse.get_name())
    fish = Fish('Нео', 3, 2)
    print(fish.get_name())
