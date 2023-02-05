import random
import numpy as np
from scipy.optimize import linprog
import csv

# Function to get constraints for a board
def get_constraints(board):
    constraints = []
    # Iterate over all cells in the board
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            # If the cell has a number, i.e. it's not a mine
            if board[row][col] != -1:
                # Get the indices of surrounding cells
                surrounding_indices = [(row + i, col + j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
                # Remove indices that are out of bounds
                surrounding_indices = [(r, c) for r, c in surrounding_indices if 0 <= r < board.shape[0] and 0 <= c < board.shape[1]]
                # Count the number of mines in surrounding cells
                surrounding_mines = [board[r][c] for r, c in surrounding_indices if board[r][c] == -1]
                if surrounding_mines:
                    constraint = [0] * (board.size)
                    # For each surrounding cell, set the constraint to 1
                    for r, c in surrounding_indices:
                        idx = r * board.shape[1] + c
                        constraint[idx] = 1
                    # The cell with the number should have the negative number of mines as its value
                    constraint[row * board.shape[1] + col] = -len(surrounding_mines)
                    constraints.append(constraint)
    # Return the constraints
    return constraints

# Function to solve the board using linear programming
def solve(board):
    n = board.size
    # Objective function is to minimize the number of mines
    c = [1] * n
    # No cells have lower bounds
    bounds = [(0, None) for _ in range(n)]
    # Get the constraints for the board
    constraints = get_constraints(board)
    # Use simplex method to solve the LP
    res = linprog(c, A_ub=constraints, b_ub=[0] * len(constraints), bounds=bounds, method='simplex')
    # Return the solution
    return res.x

# Function to play a single game of Minesweeper
def play_game(board):
    n = board.shape[0] * board.shape[1]
    # Solve the board
    x = solve(board)
    # Convert the solution to integers
    x = [int(round(xi)) for xi in x]
    # For each cell in the solution
    for i in range(n):
        # If the cell is a mine
        if x[i] == 1:
            row, col = i // board.shape[1], i % board.shape[1]
            # If the mine is in a cell with a number, the game is lost
            if board[row][col] == -1:
                return False
            # Otherwise, the cell is marked as uncovered
            else:
                board[row][col] = -2
    # The game is won
    return True

#Main function to start the game
def main():
    n_rows = 40
    n_cols = 40
    n_mines = 99
    n_games = 10
    win_count = 0
    results = []
    for game in range(n_games):
        board = np.zeros((n_rows, n_cols), dtype=int)
        for i in range(n_mines):
            row = random.randint(0, n_rows - 1)
            col = random.randint(0, n_cols - 1)
            while board[row][col] == -1:
                row = random.randint(0, n_rows - 1)
                col = random.randint(0, n_cols - 1)
            board[row][col] = -1
        for row in range(n_rows):
            for col in range(n_cols):
                if board[row][col] == -1:
                    continue
                surrounding_indices = [(row + i, col + j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
                surrounding_indices = [(r, c) for r, c in surrounding_indices if 0 <= r < n_rows and 0 <= c < n_cols]
                surrounding_mines = [board[r][c] for r, c in surrounding_indices if board[r][c] == -1]
                board[row][col] = len(surrounding_mines)
        result = play_game(board)
        if result:
            win_count += 1
            results.append(1)
        else:
            results.append(0)
    with open('game_statistics.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Result"])
        for i in range(n_games):
            writer.writerow([results[i]])
        writer.writerow(["Win Rate", win_count/n_games])
        writer.writerow(["Lose Rate", (n_games - win_count)/n_games])

if __name__ == "__main__":
    main()





