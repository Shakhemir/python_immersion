"""
Задание №2.
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра
Задание №3.
Добавьте к задачам 1 и 2 строки документации для классов.
Задание №4.
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""


class Archive:
    """Класс архивирует свойства"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls.int_list = []
            cls.str_list = []
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, int_value, str_value):
        """инициализация"""
        self.int_list.append(int_value)
        self.str_list.append(str_value)

    def __repr__(self):
        return f'Archive2({self.int_list}, {self.str_list})'

    def __str__(self):
        return f'{self.int_list}\n{", ".join(self.str_list)}'


if __name__ == '__main__':
    ar1 = Archive(1, '2')
    print(ar1)
    ar2 = Archive(3, '4')
    print(f'{ar1 = }')
    print(f'{ar2 = }')
    ar3 = Archive(5, '6')
    print(ar1 is ar2)
    print(f'{ar1 = }')
    print(f'{ar2 = }')
    print(f'{ar3 = }')
    # print(ar1)
    # help(Archive)
    # print(Archive.__doc__)
