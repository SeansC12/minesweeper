# import np
import random
from cell import Cell
import settings



def MinesweeperSolver(board):
    # Initialise the board with mines
    # Flatten the array board
    flattened_board = [inner for c in board for inner in c]
    selected_bombs = random.sample(flattened_board, int(settings.MINE_DENSITY * float((settings.ROW_COUNT ** 2))))

    # Make each cell know that they are a bomb
    for cell in selected_bombs:
        cell.is_mine = True
    
    # Make each cell know how many bombs are around it
    for row, x in enumerate(board):
        for col, current_cell in enumerate(x):
            # If cell is a bomb
            if current_cell.is_mine:
                continue

            # Cell is not a bomb
            # Check for upper row
            for i in range(-1, 2):
                try:
                    cell_to_check = board[row - 1][col + i]
                except IndexError:
                    continue

                if cell_to_check.is_mine:
                    current_cell.mines_around += 1
            
            # Check for same row
            for i in range(-1, 2):
                try:
                    cell_to_check = board[row][col + i]
                except IndexError:
                    continue

                if cell_to_check.is_mine:
                    current_cell.mines_around += 1
            
            # Check for row below
            for i in range(-1, 2):
                try:
                    cell_to_check = board[row ][col + i]
                except IndexError:
                    continue

                if cell_to_check.is_mine:
                    current_cell.mines_around += 1

    # Now that each cell knows how many bombs are around it, we can start playing the game
    # Start with cell at coordinate (0, 0)
       




























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


