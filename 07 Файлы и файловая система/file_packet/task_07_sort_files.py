"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""

import os
import shutil


def sort_files_by_type(source_directory, destination_directory):
    if not os.path.isdir(source_directory):
        print(f"Source directory '{source_directory}' does not exist.")
        return

    # Создание списка расширений для каждой категории файлов
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Documents': ['.doc', '.pdf', '.txt'],
        'Others': ['.exe', '.zip', '.rar']
    }

    if not os.path.isdir(destination_directory):
        os.makedirs(destination_directory)

    for category, extensions in file_types.items():
        category_directory = os.path.join(destination_directory, category)
        os.makedirs(category_directory, exist_ok=True)

        for file in os.listdir(source_directory):
            file_path = os.path.join(source_directory, file)
            if os.path.isfile(file_path) and os.path.splitext(file)[-1].lower() in extensions:
                shutil.move(file_path, category_directory)

    remaining_files_directory = os.path.join(destination_directory, 'Remaining Files')
    os.makedirs(remaining_files_directory, exist_ok=True)

    for file in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file)
        if os.path.isfile(file_path):
            shutil.move(file_path, remaining_files_directory)


if __name__ == '__main__':
    source_directory = 'Rand_files'
    destination_directory = 'Sorted'
    sort_files_by_type(source_directory, destination_directory)
