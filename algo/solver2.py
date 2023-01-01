import random
from cell import Cell
import settings

def MinesweeperSolver(board: list):
    known = [c for c in board if c.is_opened == True]
    boundary = [c for c in board if c in known and c]

    
