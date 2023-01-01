from cell import Cell
import settings
import sys
import random
from solver import MinesweeperSolver

def initialiseBoard(): # Initialise board arrangement
    board = list()
    for row in range(settings.ROW_COUNT): # settings.ROW_COUNT = 5
        board.append([])
        for col in range(settings.ROW_COUNT):
            board[row].append(Cell(row, col))
    return board

'''
Plan to run game each iteration, need to include solver function from solver.py
'''
def play_game(board):
    solver = MinesweeperSolver(board)
    return solver
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

# print(f"Win rate: {win_rate}")
# print(f"Lose rate: {lose_rate}")

# board = initialiseBoard()
# play_game(board)
