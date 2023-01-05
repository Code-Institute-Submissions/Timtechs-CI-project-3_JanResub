from random import randint


def new_game():
    board = []

    for x in range(6):
        board.append(["-"] * 6)

    def print_board(board):
        for row in board:
            print((" ").join(row))

    print("Welcome to Timtechs Battleships!")
    print("To play the game, choose a number between 0-5.")
    print("You have 9 turns to find the ship.")

    def random_x(board):
        return randint(0, len(board) - 1)

    def random_y(board):
        return randint(0, len(board[0]) - 1)

    ship_x = random_x(board)
    ship_y = random_y(board)

    for turn in range(9):
        guess_x = int(input("Guess X: \n"))
        guess_y = int(input("Guess Y: \n"))

        if guess_x == ship_x and guess_y == ship_y:
            print("You won!")
            break
        else:
            if (guess_x < 0 or guess_x > 5) or (guess_y < 0 or guess_y > 5):
                print("Please enter a number between 0-5")
            elif (board[guess_x][guess_y] == "X"):
                print("You already guessed this one")
            else:
                print("You missed! Hah!")
                board[guess_x][guess_y] = "X"
        if turn == 8:
            print("Game Over")
        turn =+ 1
        print_board(board)


while True:
    new_game()
    print("Do you want to play again? yes/no?")
    response = input()
    if not response == "yes":
        break
