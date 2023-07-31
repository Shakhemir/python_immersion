"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def create_argument_dict(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        try:
            hash(value)
        except TypeError:
            value = str(value)
        argument_dict[value] = key
    return argument_dict


result = create_argument_dict(arg1='value1', arg2=[1, 2, 3], arg3={1: 2, '3': 'four'})
print(result)
