import random

from packet import checkmate


def random_coords():
    x_coords = [i for i in range(1, 9)]
    y_coords = [i for i in range(1, 9)]
    random.shuffle(x_coords)
    random.shuffle(y_coords)
    return list(zip(x_coords, y_coords))


count = 0
while count < 4:
    queens_coords = random_coords()
    if checkmate.check_eight_queens(queens_coords):
        print(queens_coords)
        checkmate.draw_board(queens_coords)
        count += 1
