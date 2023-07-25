import os
import json
from functools import wraps


def save_json(func):
    """
    Декоратор, который сохраняет в файл json
    позиционные, ключевые параметры, а также
    результат работы декорируемой функции
    назвав файл именем функции
    :param func: декорируемая функция
    :return:
    """
    @wraps
    def wrapper(*args, **kwargs):
        file_name = func.__name__ + '.json'
        if os.path.isfile(file_name):
            with open(file_name, encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []
        result = func(*args, **kwargs)
        data.append({'args': args, 'kwargs': kwargs, 'result': result})
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        return result

    return wrapper

