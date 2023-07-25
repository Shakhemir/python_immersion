"""
Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.
"""

import csv
import random
import json


def generate_csv(filename):
    size = random.randint(100, 1000)
    print(f'CSV size = {size}')
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(size):
            writer.writerow([random.randint(-99, 99) for _ in range(3)])


def apply_to_csv(func):
    def wrapper(filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            result = []
            for row in reader:
                a, b, c = map(float, row)
                result.append(func(a, b, c))
                print(result)
        return result

    return wrapper


# Usage:

def log_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "function": func.__name__,
                "args": args,
                "kwargs": kwargs,
                "result": result
            }
            with open(filename, 'w') as jsonfile:
                json.dump(data, jsonfile)
            return result

        return wrapper

    return decorator


# Usage:
@log_to_json('log.json')
@apply_to_csv
def solve_quadratic_equation(a, b, c):
    if a == 0:
        return None
    # Вычисляем дискриминант
    D = (b ** 2 - 4 * a * c) ** 0.5

    # Вычисляем два решения
    sol1 = (-b - D) / (2 * a)
    sol2 = (-b + D) / (2 * a)

    return sol1, sol2


CSV_FILE = 'quad.csv'
generate_csv(CSV_FILE)
solve_quadratic_equation(CSV_FILE)
