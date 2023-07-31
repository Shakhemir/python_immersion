"""
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.
"""
import os
import json
import csv
import pickle


class Serialize:
    def __init__(self):
        self._csv_output_file = 'output.csv'
        self._json_output_file = 'output.json'
        self._pickle_output_file = 'output.pickle'
        self._data = []

    def explore_directory(self, directory):
        for root, dirs, files in os.walk(directory):
            for name in files:
                full_path = os.path.join(root, name)
                size = os.path.getsize(full_path)
                self._data.append({
                    "name": name,
                    "path": full_path,
                    "parent": root,
                    "type": "file",
                    "size": size
                })
            for name in dirs:
                full_path = os.path.join(root, name)
                size = sum(
                    os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in
                    os.walk(full_path)
                    for filename in filenames)
                self._data.append({
                    "name": name,
                    "path": full_path,
                    "parent": root,
                    "type": "dir",
                    "size": size
                })

    @property
    def _get_data(self):
        if not self._data:
            self.explore_directory('.')
        return self._data

    def save_to_json(self, file=None):
        if file is not None:
            self._json_output_file = file
        with open(self._json_output_file, 'w', encoding='utf-8') as f:
            json.dump(self._get_data, f, indent=6)

    def save_to_csv(self, file=None):
        if file is not None:
            self._csv_output_file = file
        with open(self._csv_output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self._get_data[0].keys())
            writer.writeheader()
            writer.writerows(self._get_data)

    def save_to_pickle(self, file=None):
        if file is not None:
            self._pickle_output_file = file
        with open(self._pickle_output_file, 'wb') as f:
            pickle.dump(self._get_data, f)


if __name__ == '__main__':
    ser = Serialize()
    ser.save_to_csv('test.csv')
    ser.explore_directory('../..')
    ser.save_to_json()
    ser.save_to_pickle()
