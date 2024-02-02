import numpy as np
from Player import player
from Computer import computer
from Game_Board import grid

##self.grid.board = self.game_board for others

class main:
    def __init__(self):
        self.grid = grid()
        self.player = player(self.grid.board)
        self.computer = computer(self.grid.board)

    def gameLoop(self):
        game = True ##NOTE The Board should be printed before each turn and at the end
        while game:
            ##user turn##
            self.player.userTurn()
            ##check for win##
            check = self.checkWin("X")
            check = self.checkFull()
            if check:
                break
            ##computer turn##
            self.computer.computerTurn()
            ##check for win##
            check = self.checkWin("O")
            check = self.checkFull()
            if check:
                break

    def checkWin(self, type):
        for name, condition in self.grid.win_conditions.items():
            if np.all(self.grid.board[condition == 'a'] == type):
                print(f" ----- {type} wins  ----- ")
                return True

    def checkFull(self):
        data = np.nditer(self.grid.board)
        if not "-" in data:
            print(" -----  CAT GAME  ----- ")
            print(self.grid.board)
            return True


controller = main()
controller.gameLoop()