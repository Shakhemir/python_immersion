from exceptions import PositiveIntError
from exceptions import JSONFileNameError


class PositiveInt:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def validate(self, value):
        if value is None:
            return
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if value <= 0:
            raise PositiveIntError


class JSONFileName:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def validate(self, value):
        if value is None:
            return
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть строкой')
        if not value.endswith('.json'):
            raise JSONFileNameError(value)
