def repeat(repeat_number):
    """
    Декоратор, который повторно вызывает декорируемую функцию
    :param repeat_number: количество повторов
    :return:
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(repeat_number):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return decorator
