import numpy as np
from Game_Board import grid

class player:
    def __init__(self, game_board):
        self.grid = grid()
        self.game_board = game_board


    def userTurn(self):
        turnLoop = True
        while turnLoop:
            print(self.game_board)
            userPos = self.getInput()
            validate = self.grid.validatePosition(userPos, self.game_board)
            if validate == True:
                self.placeMove(userPos)
                break
            else:
                print(f"Invalid move: {userPos}")

    def getInput(self):
        entryLoop = True
        while entryLoop:
            try:
                userPos = int(input(f"{self.grid.movement_example} \n User Choice: "))
                if 0 < userPos < 10:
                    return userPos
                else:
                    print("Use a vald integer")
            except:
                print("Use a valid integer")

    def placeMove(self, position):
        row, col = self.grid.convertPosition(position)
        self.game_board[row, col] = "X"
