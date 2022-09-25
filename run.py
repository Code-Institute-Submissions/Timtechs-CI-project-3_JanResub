"""
Imports and global variables
"""
import random

BOARD_COLUMNS_SIZE = 3
BOARD_ROW_SIZE = 1

player_board = [0, 0, 0]
computer_board = [0, 0, 0]


def main():
    """
    Function with game logic and positioning. With user input for both
    ship placement and shots.
    """
    computer_ship_loc = random.randint(0, BOARD_COLUMNS_SIZE)
    computer_board[computer_ship_loc] = 0
    user_ship_loc = input("Enter a value from 0-2 to place your ship: ")

    if user_ship_loc in [0, 1, 2]:
        return user_ship_loc
    else:
        user_ship_loc = input("Enter a value from 0-2 to place your ship: ")

    player_board[user_ship_loc] = user_ship_loc

    user_shot_locs = []

    user_shot_loc = input("Enter a value from 0-2 to shoot computer ship: ")

    if user_ship_loc not in [0, 1, 2]:
        user_shot_loc = input("Enter a value from 0-2 to shoot comp ship: ")

    if user_shot_loc not in user_shot_locs:
        user_shot_locs.append(user_shot_loc)

    if computer_board[user_ship_loc] == user_ship_loc:
        print("Victory!")

    computer_shot_loc = random.randint(0, BOARD_COLUMNS_SIZE)
    if player_board[computer_shot_loc] == user_ship_loc:
        print("You lose!")


main()
