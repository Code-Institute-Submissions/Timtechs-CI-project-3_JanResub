from random import randint

computerBoard = [0] * 100
playerBoard = [0] * 100

computerBoardCopy = [0] * 100

onGame = True

computerShot = []
playerShot = []

def main():
    playerHit = 0
    computerHit = 0

    boatPosition(playerBoard, computerBoard)

    while onGame == True:

        print(computerBoardCopy)

        playerShot = input("Choose where to shoot")
        playerShot.split(",")
        letter = playerShot[0]
        number = int(playershot[2])

        player_Shot = int(ord(letter)) - 65 + 10*(number - 1)

        if can_shoot(prevPlayerShot, player_shot) == True:

            if computerShot[player_Shot] == 1:
                hit(computerBoardCopy, player_Shot)
                print("Hit!")
                boatHitPlayer = boatHit + 1
                end_Game("Player")

            else:
                shoot(computerBoardCopy, player_Shot)
                print("Aww.. you missed.. Computers turn: ")
                computer_Shot = random.randint(0,99)
                
                if playerBoard[computer_Shot] == 1:
                    print("Computer Hit!")
                    hit(playerBoard, computer_Shot)
                    print(playerBoard)
                    boatHitComputer = boatHitComputer + 1
                    end_Game("Computer")

                else:
                    shoot(playerBoard, computer_Shot)
                    pint("Computer missed!")

def hit(grid, shot):
    grid.pop(shot)
    grid.insert(shot, "@")

def shoot(grid, shot):
    grid.pop(shot)
    grid.insert(shot, "X")

def end_Game(grid):
    if grid == "Computer":
        if grid == 14:
            onGame = False
            print("Sorry you lost")

    elif grid == "Player":
        if grid == 14:
            onGame = False
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
        x, y, direction = random.randint(0, 9),

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