import random


def check_numbers(max_answer, max_attempts):
    """
    Декоратор проверяет, входит ли в диапозон от 1 до max_answer
    загаданное число answer.
    Также с числом attempts
    :param max_answer: максимальное число для answer
    :param max_attempts: максимальное число для attempts
    :return:
    """

    def decorator(func):
        def wrapper(answer, attempts):
            if not (1 <= answer <= max_answer):
                answer = random.randint(1, max_answer)
            if not (1 <= attempts <= max_attempts):
                attempts = random.randint(1, max_attempts)
            result = func(answer, attempts)
            return result

        return wrapper

    return decorator


if __name__ == '__main__':
    """
    Пример применения декоратора
    """


    @check_numbers(100, 10)
    def guessing_game(answer, attempts):
        print('Загаданное число', answer)
        print('Число попыток', attempts)
        for _ in range(attempts):
            guess = int(input('Угадайте число: '))
            if guess == answer:
                return print('Угадали!')
            elif guess < answer:
                print('Больше')
            else:
                print('Меньше')
        print('Вы не угадали')


    guessing_game(101, 23)
