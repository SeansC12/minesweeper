import random
import settings

# TODO: Add class method for win-lose
# TODO: Code for instantiating the game
# TODO: Implement solver for game   

class Cell:
    def __init__(self, row, column, is_mine=False, mines_around=0):
        self.is_mine = is_mine
        self.is_opened = False
        self.row = row
        self.column = column
        self.mines_around = mines_around
        self.flagged = False

    def open_cell(self):
        self.is_opened = True
        return self.is_mine
    
    def flag_cell(self):
        self.flagged = True
    
