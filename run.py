from random import randint


def game_board(size):
    return [['-' for count in range(size)] for count in range(size)]


def print_board(board):
    for i in board:
        print(*i)


def place_ship(size):
    row = random.randint(0, size - 1)
    column = random.randint(0, size - 1)
    coords = row, column
    return list(coords)


def main():
    board = game_board(5)
    print_board(board)
    ship = place_ship(4); ship


main()
