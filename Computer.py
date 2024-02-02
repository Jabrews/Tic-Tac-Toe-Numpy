import numpy as np
from Game_Board import grid
from Extra import win_conditions

moves = [
            {"Position1" : 1, "Valid": True},
            {"Position2": 2, "Valid": True},
            {"Position3": 3, "Valid": True},
            {"Position4": 4, "Valid": True},
            {"Position5": 5, "Valid": True},
            {"Position6": 6, "Valid": True},
            {"Position7": 7, "Valid": True},
            {"Position8": 8, "Valid": True},
            {"Position9": 9, "Valid": True}
        ]

class computer:
    def __init__(self, game_board):
        self.grid = grid()
        self.game_board = game_board
        self.possible_moves = moves
        self.win_cond = win_conditions

    def updatePos(self, position):
        row, col = self.grid.convertPosition(position)
        self.game_board[row, col] = "O"

    def checkMoves(self):
        for move in self.possible_moves:
            position = move[list(move.keys())[0]]  # Extract the position integer
            row, col = self.grid.convertPosition(position)
            if self.game_board[row][col] in ["X", "O"]:
                move["Valid"] = False
            else:
                move["Valid"] = True

    def computerTurn(self):
        winningState = False
        blockingState = False
        self.checkMoves()
        ##get all valid position##
        for move in self.possible_moves:
            position = move[list(move.keys())[0]]
            if move["Valid"]:
                if not winningState:
                    winningState = self.isWin(position)
                    if winningState:
                        print("making win state move")
                        self.updatePos(position)
                        return
                if not blockingState:
                    blockingState = self.needs_blocking(position)
                    if blockingState:
                        print("making blocking state move")
                        self.updatePos(position)
                        return

        for move in self.possible_moves:
            position = move[list(move.keys())[0]]  # Extract the position integer from the current move
            if move["Valid"]:
                print("Fallback move")
                self.updatePos(position)
                return



    ###### WIN STATE #########
    def isWin(self, position):
        # Create a copy of the grid to simulate the move
        grid_copy = np.copy(self.game_board)
        row, col = self.grid.convertPosition(position)
        grid_copy[row, col] = "O"
        # Check for a win condition
        for name, condition in self.win_cond.items():
            if np.all(grid_copy[condition == 'a'] == "O"):
                return True

        return False

    def terminal(self, position):
        valid = self.isWin(position)
        if valid == True:
            row, col = self.grid.convertPosition(position)
            self.grid[row, col] = "O"
            return True
        else:
            return False
    #\\\\\\\\\\\\\\\\\\\\\\\\#

    #\\\\\Blocking Move\\\\\\#
    def needs_blocking(self, position):
        grid_copy = np.copy(self.game_board)
        row, col = self.grid.convertPosition(position)  # Calculate row and column index

        grid_copy[row, col] = "X"

        for name, condition in self.win_cond.items():
            if np.all(grid_copy[condition == 'a'] == "X"):
                return True

        return False
    #\\\\\\\\\\\\\\\\\\\\\\\#

