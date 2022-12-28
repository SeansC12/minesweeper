from cell import Cell
import settings
import sys
import random
from solver import MinesweeperSolver

def row_max(x): # Function that calculates the number of cells in each row
    return (2*x + 1)

def initialiseBoard(): # Initialise board arrangement
    for x in range(settings.ROW_COUNT): # settings.ROW_COUNT = 5
        for y in range(row_max(x)):
            c = Cell(x, y) # Initialises a cell for each (x, y)
'''
Plan to run game each iteration, need to include solver function from solver.py
'''
def play_game(board):
    solver = MinesweeperSolver(board)
    while not solver.solve():
        pass
    return 

def play_games(num_games):
    wins = 0
    losses = 0
    initialiseBoard()

    if not any(c.is_opened == True for c in Cell.all):
        random_cell = random.choice(Cell.all)
        random_cell.left_click_actions()

    if Cell.clicks == 1:
        Cell.randomise_mines()
    for i in range(num_games):
        board = Cell.all
        play_game(board)
        if Cell.IsWin == True:
            wins += 1
            print(f"Wins: {wins}")
        else:
            losses += 1
            print(f"Losses: {losses}")
    return wins, losses

wins, losses = play_games(100)
win_rate = wins / (wins + losses)
lose_rate = losses / (wins + losses)
print(f"Win rate: {win_rate}")
print(f"Lose rate: {lose_rate}")




        
        
        
        

