import numpy as np
import random
from cell import Cell
import settings

class BombError(Exception):
    def __init__(self, message='You just hit a bomb'):
        # Call the base class constructor with the parameters it needs
        super(BombError, self).__init__(message) 

def MinesweeperSolver(board):
    def dfs(board, row, col):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board):
            return
        if board[row][col].is_mine:
            raise BombError
        if board[row][col].is_opened:
            raise BombError
            return
        if board[row][col].mines_around > 0:
            board[row][col].open_cell()
            return
        board[row][col].open_cell()
        for i in range(-1, 2):
            for j in range(-1, 2):
                dfs(board, row + i, col + j)
    
    for i in range(len(board)):
        for j in range(len(board)):
            if not board[i][j].is_mine and not board[i][j].is_opened:
                dfs(board, i, j)


# def get_surroundings(board, row, col):
#     surroundings = list()
#     for i in range(-1, 0, 1):
#         for j in range(-1, 0, 1):
#             if i == j and i == 0:
#                 continue
#             try:
#                 surroundings.append(board[row + i][col + j])
#             except IndexError:
#                 continue
    
#     return surroundings

# def MinesweeperSolver(board):
#     # Start with cell 0,0
#     board[0][0].open_cell()
#     # Now that each cell knows how many bombs are around it, we can start playing the game
#     unsolved_cells = list()

#     for cell in [inner for c in board for inner in c]:
#         if cell.is_opened or cell.flagged:
#             continue
#         unsolved_cells.append(cell)
    
#     while unsolved_cells:
#         for c in unsolved_cells:
#             row = c.row
#             col = c.column

#             # Standardise the structure for future reference (they know what cell, if encountered for
#             # the second time, is supposed to be at what position)
#             surrounding_cells = get_surroundings(board, row, col)

#             # Define the structure needed for the simultaneous equation to work
#             structure = list()
            
#             # Intermediate step in order to build the coefficient matrix
#             cells_to_simul_eqn = list()
            
#             coefficient_matrix = list()
#             resulting_values = list()

#             # Get the surrounding numbered cells
#             for cell in surrounding_cells:
#                 if not cell.is_opened and not cell.is_mine:
#                     # It is a numbered cell
#                     surrounding_number_cells = get_surroundings(board, cell.row, cell.column)
                    
#                     # Initialise new simultaneous equation
#                     # I am adding 9 placeholder values so I can keep track of which one is x1 and which
#                     # one is x2.
#                     # This works because I have to remember what x value it is, for example x1 or x2.
#                     # Hence, I can structure the coefficient vector properly
#                     cells_to_simul_eqn.append([0, 0, 0, 0, 0, 0, 0, 0])
                    
#                     print(f"len {len(surrounding_cells)}")

#                     for i in surrounding_number_cells:
#                         if not i.is_opened and not i.is_mine: # This basically gives us like that unknown cell
#                             # If cell is in structure, we change the default value (0) of the cells_to_simul_eqn subarray
#                             # with this cell, so it lines up
#                             if i in structure:
#                                 cells_to_simul_eqn[-1][structure.index(i)] = i
#                             else:
#                                 cells_to_simul_eqn[-1][len(structure)] = i
#                                 structure.append(i)
                    
#                     resulting_values.append(cell.mines_around)

#             # Time to build the coefficient matrix
#             for a in cells_to_simul_eqn:
#                 coefficient_matrix.append([])
#                 for b in a:
#                     if b == 0:
#                         coefficient_matrix[-1].append(0)
#                     else:
#                         coefficient_matrix[-1].append(1)
            
#             # coefficient_matrix = np.array(coefficient_matrix)
#             # resulting_values = np.array(resulting_values)

#             # Use numpy to solve the simultaneous equation
#             print(coefficient_matrix, resulting_values)
#             solved_eqn = list(list(np.linalg.lstsq(coefficient_matrix, resulting_values, rcond=None))[0])
#             # solved_eqn = list(np.linalg.solve(coefficient_matrix, resulting_values))
#             print(f"Solved eqn: {solved_eqn}")
#             exit()





























# class MinesweeperSolver2:
#     def __init__(self, board):
#         self.board = board
#         self.unknown_cells = [c for c in self.board if not c.is_opened]

#     def solve(self):
#         coefficient_matrix = [] # Matrix with the unknown cells
#         result_vector = [] # Mine-values of the known cells

#         for cell in self.board:
                
#             if cell.is_opened:
#                 unknown_cells = [c for c in cell.surrounded_cells if c.is_opened == False]

#                 if not unknown_cells:
#                     continue
        
#                 coefficients = [1 if c in unknown_cells else 0 for c in self.unknown_cells] # If the unknown cell is within the neighbourhood, have a 1 coefficient and 0 otherwise.
#                 coefficient_matrix.append(coefficients)

#                 result_vector.append(cell.surrounded_cells_mines_length) 
        
#         try:
#             solution = np.linalg.solve(coefficient_matrix, result_vector)
#         except np.linalg.LinAlgError:
#             return False
        
#         if not all(x == 0 or x == 1 for x in solution):
#             for i, cell in enumerate(self.unknown_cells):
#                 cell.flagged = bool(solution[i])
            
#             for cell in self.unknown_cells:
#                 if cell.flagged == False:
#                     cell.is_opened = True

#         return True


