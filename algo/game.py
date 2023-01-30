from cell import Cell
import settings
import sys
import random
from solver import MinesweeperSolver

class BombError(Exception):
    def __init__(self, message='You just hit a bomb'):
        # Call the base class constructor with the parameters it needs
        super(BombError, self).__init__(message) 

def initialiseBoard(): # Initialise board arrangement
    board = list()
    for row in range(settings.ROW_COUNT): # settings.ROW_COUNT = 5
        board.append([])
        for col in range(settings.ROW_COUNT):
            board[row].append(Cell(row, col))
    
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
            surroundings = list()
            # If cell is a bomb
            if current_cell.is_mine:
                continue
            
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    
                    try:
                        surroundings.append(board[row + i][col + j])
                    except IndexError:
                        continue
            
            current_cell.mines_around = sum(c.is_mine for c in surroundings)

    return board

'''
Plan to run game each iteration, need to include solver function from solver.py
'''
def play_game(board):
    try:
        MinesweeperSolver(board)
        return True
    except:
        return False
    # True is win, False is lost

def play_games(num_games):
    win_count = 0
    loss_count = 0

    for _ in range(num_games):
        board = initialiseBoard()
        status = play_game(board)
        if status:
            win_count += 1
        else:
            loss_count += 1
    
    return win_count, loss_count

win_count, loss_count = play_games(100)
win_rate = win_count / (win_count + loss_count)
lose_rate = loss_count / (win_count + loss_count)

print(f"Win rate: {win_rate}")
print(f"Lose rate: {lose_rate}")
