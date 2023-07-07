"""
Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
import random


def random_fill_file(file_name: str, row_num: int):
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(row_num):
            print(f'{i}: {random.randint(-1000, 1000)} | {random.uniform(-1000, 1000)}', file=f)


if __name__ == '__main__':
    random_fill_file('1.txt', 15)
