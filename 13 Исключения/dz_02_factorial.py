""" Проверка на правильное имя файла JSON """

import json
import random
from collections import deque
from descriptors import JSONFileName


class Factorial:
    file_json = JSONFileName()

    def __init__(self, k, output_json: str):
        self.last_k = deque(maxlen=k)
        self.file_json = output_json

    def __call__(self, num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        self.last_k.append((num, result))
        return result

    @property
    def last_results(self):
        return self.last_k

    def __repr__(self):
        return str(self.last_results)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file_json, 'w', encoding='utf-8') as f:
            json.dump(dict(self.last_results), f, indent=2)


if __name__ == '__main__':
    with Factorial(9, 'output.jsn') as f:
        for _ in range(10):
            print(f(random.randint(2, 10)))
    print(f)
