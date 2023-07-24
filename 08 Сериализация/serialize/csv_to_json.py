"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""

import csv
import json


def csv_to_json(csv_file, json_file):
    with (open(csv_file, encoding='utf-8') as csv_f,
          open(json_file, 'w', encoding='utf-8') as json_f):
        csv_data = csv_f.readlines()
        print('[', file=json_f)
        for i, line in enumerate(csv_data):
            line = line.strip()
            if i == 0:
                titles = line.split(',')
                titles.append('Hash')
            else:
                user_id, name, level = line.split(',')
                rec = user_id.zfill(10), name.capitalize(), level, hash(name + user_id)
                rec_dict = dict(zip(titles, rec))
                print(json.dumps(rec_dict), file=json_f, end=',\n' if (i < len(csv_data) - 1) else '\n')
        print(']', file=json_f)


if __name__ == '__main__':
    csv_to_json('base.csv', 'base_new.json')
