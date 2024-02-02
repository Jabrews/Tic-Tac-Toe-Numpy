import numpy as np
from Extra import win_conditions

class grid:
    def __init__(self):
        self.board = np.array([["-","-","-"],["-","-","-"],["-","-","-"]])
        self.movement_example = np.array([[1,2,3],[4,5,6],[7,8,9]])
        self.win_conditions = win_conditions

    def convertPosition(self, position):
        position -= 1
        row = position // 3  # Calculate row index
        col = position % 3  # Calculate column index
        return row, col

    def validatePosition(self, position, game_board):
        row, col = self.convertPosition(position)
        if game_board[row, col] == "-":
            return True
