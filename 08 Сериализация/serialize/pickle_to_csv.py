"""
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестирования возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""

import pickle
import csv


def pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)
    with open(csv_file, 'w', encoding='utf-8') as csv_f:
        csv_writer = csv.DictWriter(csv_f, data[0].keys(), dialect='excel')
        csv_writer.writeheader()
        csv_writer.writerows(data)
    print(csv_writer.fieldnames)


if __name__ == '__main__':
    pickle_to_csv('base_new.pickle', 'base_new.csv')
