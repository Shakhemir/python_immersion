"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла
"""


def split_abs_path(abs_path: str) -> tuple:
    path_name, ext = abs_path.split('.')
    *path, name = path_name.split('/')
    return '/'.join(path), name, ext


path = '/Users/shakh/MEGAsync/Python/GB_Python/Python_Immersion_DZ/DZ_05/dz_01_path.py'
print(split_abs_path(path))
