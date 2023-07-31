"""
Доработаем задачи 5-6. Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
- Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
"""

from task_06_animals_2 import Horse
from task_06_animals_2 import Fish
from task_06_animals_2 import Bird


class Factory:
    @staticmethod
    def create_animal(animal_class, *args):
        if not isinstance(animal_class, str):
            animal_class = animal_class.__name__
        match animal_class:
            case 'Horse':
                return Horse(*args)
            case 'Fish':
                return Fish(*args)
            case 'Bird':
                return Bird(*args)


if __name__ == '__main__':
    horse = Factory.create_animal(Horse, 'Mustang', 5, 'speed')
    print(horse.get_name())
    bird = Factory.create_animal('Bird', 'Chirik', 1, 15)
    print(bird.get_speed())
    fish = Factory.create_animal(Fish, 'Neo', 5, 10)
    print(fish.get_age())
