"""
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
"""

import os
import json
import csv
import pickle


def explore_directory(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            full_path = os.path.join(root, name)
            size = os.path.getsize(full_path)
            result.append({
                "name": name,
                "path": full_path,
                "parent": root,
                "type": "file",
                "size": size
            })
        for name in dirs:
            full_path = os.path.join(root, name)
            size = sum(
                os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(full_path)
                for filename in filenames)
            result.append({
                "name": name,
                "path": full_path,
                "parent": root,
                "type": "dir",
                "size": size
            })
    return result


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=6)


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    data = explore_directory("..")
    save_to_json(data, "output.json")
    save_to_csv(data, "output.csv")
    save_to_pickle(data, "output.pickle")
