"""
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""

import csv
import json


def json_to_csv(json_file, csv_file):
    with open(json_file) as json_f:
        base = json.load(json_f)
    with open(csv_file, 'w', encoding='utf-8') as csv_f:
        base_csv = csv.writer(csv_f, dialect='excel')
        base_csv.writerow(('ID', 'Name', 'Level'))
        for level, user in base.items():
            for user_id, name in user.items():
                row = user_id, name, level
                base_csv.writerow(row)


if __name__ == '__main__':
    json_to_csv('base.json', 'base.csv')
