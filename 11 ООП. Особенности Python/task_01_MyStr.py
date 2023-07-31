"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""
import os
from time import time


class MyStr(str):
    """Класс Моя Строка с доп возможностями"""

    def __new__(cls, text):
        """Контроль создания экземпляра для добавления доп возможностей"""
        instance = super().__new__(cls, text)
        instance.author = os.getlogin()
        instance.created_time = time()
        return instance


if __name__ == '__main__':
    my_str = MyStr('test')
    print(f'{my_str}\t{my_str.author}\t{my_str.created_time}')
