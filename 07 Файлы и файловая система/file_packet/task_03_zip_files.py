"""
Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""

NUMS_FILE = '1.txt'
NAMES_FILE = 'names.txt'


def mul_nums_names(nums: str, names: str) -> str:
    nums = nums.split(':')[1].strip()
    x, y = nums.split('|')
    name = names.split(':')[1].strip()
    mul = int(x) * float(y)
    if mul < 0:
        result = f'{name.lower()} {-mul}'
    else:
        result = f'{name.upper()} {int(mul)}'
    return result


def zip_files(result_file):
    with (
        open(result_file, 'w', encoding='utf-8') as res_f,
        open(NUMS_FILE, 'r', encoding='utf-8') as nums_f,
        open(NAMES_FILE, 'r', encoding='utf-8') as names_f,
    ):
        i = 0
        go_1 = go_2 = True
        while go_1 or go_2:
            nums = nums_f.readline().rstrip()
            if not nums:
                go_1 = False
                nums_f.seek(0)
                nums = nums_f.readline().rstrip()
            names = names_f.readline().rstrip()
            if not names:
                go_2 = False
                names_f.seek(0)
                names = names_f.readline().rstrip()
            if go_1 or go_2:
                print(f'{i}: {mul_nums_names(nums, names)}', file=res_f)
                i += 1


if __name__ == '__main__':
    zip_files('zip_file.txt')
