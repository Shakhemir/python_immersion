"""
Напишите функцию для транспонирования матрицы
"""


def transpose_matrix(matrix):
    # Получаем количество строк и столбцов исходной матрицы
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу с переставленными размерами (транспонированную)
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return transposed_matrix


# Пример использования:
matrix = [[1, 2, 3, True, 'abc'],
          [4, 5, 6, (0, 1), {3, 4}],
          [7, 8, 9, {1: 2, '3': '4'}, False]]

transposed = transpose_matrix(matrix)
print("Исходная матрица:")
for row in matrix:
    print(row)

print("Транспонированная матрица:")
for row in transposed:
    print(row)
