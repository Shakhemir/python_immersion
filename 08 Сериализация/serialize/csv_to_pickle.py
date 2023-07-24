"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
"""

import pickle


def print_csv_as_pickle(csv_file):
    with open(csv_file) as f:
        data = f.readlines()
    print(pickle.dumps(data))


if __name__ == '__main__':
    print_csv_as_pickle('base_new.csv')
