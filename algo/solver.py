import numpy as np
import random
from cell import Cell

class MinesweeperSolver:
    def __init__(self, board):
        self.board = board
        self.unknown_cells = [c for c in self.board if not c.is_opened]

    def solve(self):
        coefficient_matrix = [] # Matrix with the unknown cells
        result_vector = [] # Mine-values of the known cells

        for cell in self.board:
                
            if cell.is_opened:
                unknown_cells = [c for c in cell.surrounded_cells if c.is_opened == False]

                if not unknown_cells:
                    continue
        
                coefficients = [1 if c in unknown_cells else 0 for c in self.unknown_cells] # If the unknown cell is within the neighbourhood, have a 1 coefficient and 0 otherwise.
                coefficient_matrix.append(coefficients)

                result_vector.append(cell.surrounded_cells_mines_length) 
        
        try:
            solution = np.linalg.solve(coefficient_matrix, result_vector)
        except np.linalg.LinAlgError:
            return False
        
        if not all(x == 0 or x == 1 for x in solution):
            for i, cell in enumerate(self.unknown_cells):
                cell.flagged = bool(solution[i])
            
            for cell in self.unknown_cells:
                if cell.flagged == False:
                    cell.is_opened = True

        return True


