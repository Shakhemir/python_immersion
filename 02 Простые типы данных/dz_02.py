""" Задание 1.
Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата
"""

def to_hex(num: int) -> str:
    hex_symbols = '0123456789abcd'
    result = ''
    while num > 16:
        div, mod = divmod(num, 16)
        result = hex_symbols[mod] + result
        num = div
    result = hex_symbols[num] + result
    return result


a = int(input('Введите целое число: '))
print(f'{hex(a)[2:]=} == {to_hex(a)=}')



""" Задание 2.
Напишите программу, которая принимает две строки
вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму
и *произведение дробей. Для проверки своего
кода используйте модуль fractions.
"""

import fractions

f1 = fractions.Fraction(*map(int, input('Введите первую дробь (a/b): ').split('/')))
f2 = fractions.Fraction(*map(int, input('Введите вторую дробь (a/b): ').split('/')))
print(f'{f1} + {f2} = {f1 + f2}')
print(f'{f1} * {f2} = {f1 * f2}')