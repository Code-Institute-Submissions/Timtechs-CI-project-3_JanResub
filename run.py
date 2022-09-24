import random

computerBoard = [0] * 100
playerBoard = [0] * 100

computerBoardCopy = [0] * 100

ONGAME = True

computerShot = []
playerShot = []


def main():
    player_Hit = 0
    compHit = 0

    boatPositions(playerBoard)
    boatPositions(computerBoard)

    while ONGAME:

        print(computerBoardCopy)

        playerShot = input("Choose where to shoot")
        playerShot.split(",")
        letter = playerShot[0]
        number = int(playerShot[2])

        player_Shot = int(ord(letter)) - 65 + 10*(number - 1)

        if can_shoot(player_Hit, playerShot) is True:

            if computerShot[player_Shot] == 1:
                hit(computerBoardCopy, player_Shot)
                print("Hit!")
                player_Hit = player_Hit + 1
                end_Game("Player")

            else:
                shoot(computerBoardCopy, player_Shot)
                print("Aww.. you missed.. Computers turn: ")
                computer_Shot = random.randint(0, 99)

                if playerBoard[computer_Shot] == 1:
                    print("Computer Hit!")
                    hit(playerBoard, computer_Shot)
                    print(playerBoard)
                    compHit = compHit + 1
                    end_Game("Computer")
                else:
                    shoot(playerBoard, computer_Shot)
                    print("Computer missed!")
        else:
            print("error")


def hit(grid, shot):
    grid.pop(shot)
    grid.insert(shot, "@")


def shoot(grid, shot):
    grid.pop(shot)
    grid.insert(shot, "X")


def end_Game(grid):
    if grid == "Computer":
        if grid == 14:
            ONGAME = False
            print("Sorry you lost")

    elif grid == "Player":
        if grid == 14:
            ONGAME = False
            print("Victory!")


def can_shoot(List, shot):
    for x in range(len(list)):
        if List[x] == shot:
            print("You struck here already")
            return False
    List.append(shot)
    return True


def boatPositions(grid):
    for n in range(2, 6):
        x, direction = random.randint(0, 9), random.randint(0, 9),
        random.randint(0, 1)
        while cant_Place_Boat(n, x, direction, grid):
            x, direction = random.randint(0, 9), random.randint(0, 9),
            random.randint(0, 1)
        boatPosition(n, x, direction, grid)


def boatPosition(length, x, direction, grid):
    if direction == 0:
        for i in range(length):
            position = x + 10
            grid.pop(position)
            grid.insert(position, 1)
            position = position + 1

    if direction == 1:
        for i in range(length):
            position = x + 10
            grid.pop(position)
            grid.insert(position, 1)
            position = position + 10


def cant_Place_Boat(length, x, direction, grid):
    return direction == 0 and x + length >= 10 or direction == 1


main()
