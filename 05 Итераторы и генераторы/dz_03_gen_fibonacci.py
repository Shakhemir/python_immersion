"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()

N = 20
fibonacci_sequence = [next(fib_gen) for _ in range(N)]
print(fibonacci_sequence)
