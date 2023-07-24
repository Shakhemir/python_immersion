"""
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""

import json
import os
import pickle


def json_to_pickles(path='.'):
    list_dir = os.listdir(path)
    for file in list_dir:
        file_name, ext = file.split('.')
        if ext == 'json':
            print(file)
            pickle_file_name = f'{file_name}.pickle'
            with (open(file, encoding='utf-8') as json_f,
                  open(pickle_file_name, 'wb') as pickle_f):
                data = json.load(json_f)
                print(type(data), data)
                pickle.dump(data, pickle_f)


if __name__ == '__main__':
    json_to_pickles()
