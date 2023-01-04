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


def player_guess():
    row = int(input("X: \n")) - 1
    cloumn = int(input("Y: \n")) - 1
    return (row, column)


def update_board(guess, guesses, board, ship):
    if guess in guesses:
        print("You already tried that.")
        return board
    guesses.append(guess)
    if guess in ship:
        print("You hit a ship!")
        board[guess[0]][guess[1]] = "X"
        ship.remove(guess)
        return board
    print("You missed! Hah!")
    return board


def main():
    board = game_board(5)
    print_board(board)
    ship = place_ship(4); ship
    x = player_guess(); x
    guesses = []
    our_guess = player_guess()
    board = update_board(our_guess, guesses, board, ship)
    print_board(board)


main()
