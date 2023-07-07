"""
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.

✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.

✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

import os
import random
import string

PATH = 'Rand_files'


def generate_random_name(min_length, max_length, extension):
    file_name_length = random.randint(min_length, max_length)
    file_name = ''.join(random.choices(string.ascii_lowercase, k=file_name_length)) + extension
    return file_name


def create_files_with_extension(extension, min_name_length=6, max_name_length=30,
                                min_byte_count=256, max_byte_count=4096, file_count=42, path=PATH):
    existing_files = set(os.listdir(path))
    for _ in range(file_count):
        file_name = generate_random_name(min_name_length, max_name_length, extension)
        while file_name in existing_files:
            file_name = generate_random_name(min_name_length, max_name_length, extension)
        byte_count = random.randint(min_byte_count, max_byte_count)
        file_name = os.path.join(path, file_name)
        with open(file_name, 'wb') as file:
            random_bytes = os.urandom(byte_count)
            file.write(random_bytes)

        print(f"Создан файл: {file_name}, размер: {byte_count} байтов")


def generate_files_with_extensions(extensions, file_counts, path=PATH):
    for extension, file_count in zip(extensions, file_counts):
        create_files_with_extension(extension, file_count=file_count, path=path)


if __name__ == '__main__':
    # create_files_with_extension('.txt', min_name_length=8, max_name_length=20,
    #                             min_byte_count=512, max_byte_count=2048, file_count=10)
    extensions = ['.txt', '.doc', '.jpg']
    file_counts = [10, 5, 8]
    generate_files_with_extensions(extensions, file_counts)
