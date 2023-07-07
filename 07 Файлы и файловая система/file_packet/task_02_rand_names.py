"""
Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
import random

there_is_vowel_letter = False
VOWEL_LETTERS = 'aeiou'


def random_char(letters_left: int):
    global there_is_vowel_letter
    result = chr(random.randint(97, 122))
    if result in VOWEL_LETTERS:
        there_is_vowel_letter = True
    if letters_left == 1 and not there_is_vowel_letter:
        result = random.choice(VOWEL_LETTERS)
    return result


def random_names_to_file(file_name: str, row_num: int):
    global there_is_vowel_letter
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(row_num):
            there_is_vowel_letter = False
            name_len = random.randint(4, 7)
            rand_name = ''.join((random_char(name_len - i) for i in range(name_len)))
            print(f'{i}: {rand_name.capitalize()}', file=f)


if __name__ == '__main__':
    random_names_to_file('names.txt', 20)
