"""
Шахматный модуль
"""


def check_eight_queens(coordinates):
    if len(coordinates) != 8:
        print('Программа должна получать на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей')
        return False
    for i in range(8):
        for j in range(i + 1, 8):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
    return True


def draw_board(coordinates):
    """
    Рисуем доску с ферзями
    """
    board = [['-' for _ in range(8)] for _ in range(8)]  # Создаем пустую доску

    for x, y in coordinates:
        board[x - 1][y - 1] = 'Q'  # Расставляем ферзей на доске

    # Выводим доску в консоль
    print('   ' + ' '.join([chr(65 + i) for i in range(8)]))  # Выводим заголовок с буквенными обозначениями столбцов

    for i, row in enumerate(board, 1):
        print(f'{i}  ' + ' '.join(row))  # Выводим номер строки и содержимое строки доски


if __name__ == '__main__':
    # Координаты
    queens_coords = ((1, 1), (2, 7), (3, 5), (4, 8), (5, 2), (6, 4), (7, 6), (8, 3))

    draw_board(queens_coords)
    if check_eight_queens(queens_coords):
        print("Ферзи не бьют друг друга")
    else:
        print("Ферзи бьют друг друга")
