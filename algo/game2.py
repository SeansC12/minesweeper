from cell import Cell
import random
from typing import List
import random
import settings

class Board: 
    def __init__(self, rows: int, cols: int, mines: int):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell(i, j) for j in range(cols)] for i in range(rows)]

    def add_mines(self):
        flattened_board = [inner for c in self.board for inner in c] 
        mines = random.sample([c for c in flattened_board if c.is_opened == True], self.mines)
        for cell in mines:
            cell.is_mine == True

    def get_surroundings(self, row: int, col: int) -> List[Cell]:
        surroundings = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == j == 0:
                    continue
                surroundings.append(self.board[i][j])
        return surroundings

    def get_mine_value(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.board[i][j]
                if cell.is_mine == True:
                    continue
                surroundings = self.get_surroundings(cell.row, cell.column)

                cell.mines_around = sum(c.is_mine for c in surroundings)

    def open_cell(self, row: int, col: int) -> int:

        cell = self.board[row][col]
        cell.is_opened = True
        return cell.mines_around

    def get_opened_cells(self) -> List[Cell]:
        return [cell for row in self.board for cell in row if cell.is_opened == True]

    def get_unopened_cells(self) -> List[Cell]:
        return [cell for row in self.board for cell in row if cell.is_opened == False]
        
