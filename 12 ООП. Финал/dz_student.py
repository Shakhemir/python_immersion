"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.
"""
import csv
import random

from descriptors import Str
from descriptors import Range


class Student:
    surname = Str()
    name = Str()
    middlename = Str()
    subjects = None

    def __init__(self, full_name: str):
        self.surname, self.name, self.middlename = full_name.split()
        self.subjects = Subjects()

    @property
    def average_grade(self):
        sum_grades = 0
        for subject in self.subjects.subjects:
            sum_grades += subject.grade
        return sum_grades / len(self.subjects.subjects)

    def __repr__(self):
        return f'{self.surname} {self.name} {self.middlename}'


class Subject:
    grade = Range(2, 6)

    def __init__(self, subject_name):
        self._name = subject_name
        self.grade = None
        self._tests = []

    @property
    def name(self):
        return self._name

    @property
    def tests(self):
        return self._tests

    def set_grade(self, number):
        self.grade = number

    def add_test_grade(self, number):
        test_grade = Range(0, 101)
        test_grade = number
        self._tests.append(test_grade)

    @property
    def average_tests(self):
        return sum(self.tests) / len(self.tests)

    def __repr__(self):
        return f'{self.name}, оценка: {self.grade}, тесты: {self.average_tests:.2f}'


class Subjects:
    CSV_FILE = 'subjects.csv'

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        with open(cls.CSV_FILE, encoding='utf-8', newline='') as f:
            csv_reader = csv.reader(f)
            cls._subjects = tuple(Subject(subject[0]) for subject in csv_reader)
        return instance

    @property
    def subjects(self):
        return list(self._subjects)

    def __repr__(self):
        return self.subjects

    def __str__(self):
        return str(self.subjects)


def fill_grades(student: Student):
    for subject in student.subjects.subjects:
        subject.set_grade(random.randint(2, 5))
        for _ in range(random.randrange(5, 10)):
            subject.add_test_grade(random.randint(0, 100))


if __name__ == '__main__':
    students_names = 'Иванов Баран Волкович', 'Козлова Овечка Рогатая', 'Мормонкин Альберт Бульбулич'
    students = [Student(fio) for fio in students_names]
    for student in students:
        fill_grades(student)
        print(student)
        print(student.subjects)
        print(f'Средняя оценка: {student.average_grade:.2f}')
