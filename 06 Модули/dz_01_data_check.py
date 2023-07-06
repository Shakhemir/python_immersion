from datetime import datetime
from calendar import isleap
import sys


def check_date(user_date: str):
    try:
        day, month, year = map(int, user_date.split('.'))
        datetime(day=day, month=month, year=year)
        return True
    except ValueError:
        return False


def check_year(user_date: str):
    try:
        *_, year = map(int, user_date.split('.'))
        return isleap(year)
    except ValueError:
        return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_date = sys.argv[1]
    else:
        input_date = input('Введите дату в формате DD.MM.YYYY: ')
    print(check_date(input_date))
    print(check_year(input_date))
