from random import randint

computerBoard = [0] * 50
playerBoard = [0] * 50

computerBoardCopy = [0] * 50

computerShot = []
playerShot = []

def main():
    playerHit = 0
    computerHit = 0

    boatPosition(playerBoard, computerBoard)

def boatPosition(length, x, y, direction, grid):
    if direction == 0:
        for i in range(length):
            position = x + 5*y
            grid.pop(position)
            grid.insert(position, 1)
            position = position + 1

    if direction == 1:
        for i in range(length):
            position = x + 5*y
            grid.pop(position)
            grid.insert(position, 1)
            position = position + 5