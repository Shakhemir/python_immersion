"""
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
"""
import random
from typing import List


class Matrix:
    """Класс Матрица со всеми необходимыми методами"""
    MIN_INT = 0
    MAX_INT = 99

    def __init__(self, rows, columns, random_fill=True):
        """
        Инициализация матрицы
        :param rows: кол-во строк
        :param columns: кол-во столбцов
        """
        self.rows = rows
        self.columns = columns
        self.matrix: List[List[int]] = []
        self._max_digit = 1
        self.__fill_matrix(random_fill)

    def __fill_matrix(self, random_fill=True):
        """Заполнение матрицы случайными значениями или нулями"""
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                if random_fill:
                    element = random.randint(self.MIN_INT, self.MAX_INT)
                    self._max_digit = max(self._max_digit, len(str(element)))
                else:
                    element = 0
                row.append(element)
            self.matrix.append(row)

    def __str__(self):
        result = ''
        for i in range(self.rows):
            row = self.matrix[i]
            str_row = ' | '.join(map(lambda s: str(s).ljust(self._max_digit), row))
            result += str_row + '\n'
        return result

    def __repr__(self):
        return f'Matrix{self.rows, self.columns}:\n{self}'

    def __eq__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return False
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result_matrix = Matrix(self.rows, self.columns, False)
            for i in range(self.rows):
                for j in range(self.columns):
                    result_matrix.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                    result_matrix._max_digit = max(result_matrix._max_digit, len(str(result_matrix.matrix[i][j])))
            return result_matrix
        else:
            raise ValueError("Для сложения матрицы должны иметь одинаковые размеры.")

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице.")
        result_matrix = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result_matrix.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                result_matrix._max_digit = max(result_matrix._max_digit, len(str(result_matrix.matrix[i][j])))
        return result_matrix


if __name__ == '__main__':
    matr1 = Matrix(5, 4)
    print(f'{matr1 = }')
    matr2 = Matrix(5, 4)
    print(f'{matr2 = }')
    print(f'{matr1 == matr2 = }')
    print(f'{matr1 + matr2 = }')
    matr3 = Matrix(4, 3)
    print(f'{matr3 = }')
    print(f'{matr1 * matr3 = }')
