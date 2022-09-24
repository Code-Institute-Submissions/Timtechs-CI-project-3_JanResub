from random import randint

computerBoard = [0] * 50
playerBoard = [0] * 50

computerBoardCopy = [0] * 50

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
                computer_Shot = random.randint(0,49)
                
                if playerBoard[computer_Shot] == 1:
                    print("Computer Hit!")
                    hit(playerBoard, computer_Shot)
                    print(playerBoard)
                    boatHitComputer = boatHitComputer + 1
                    end_game("Computer")

                else:
                    shoot(playerBoard, computer_Shot)
                    pint("Computer missed!")

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