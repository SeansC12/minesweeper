class BombError(Exception):
    def __init__(self, message='You just hit a bomb'):
        # Call the base class constructor with the parameters it needs
        super(BombError, self).__init__(message) 

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
        if self.is_mine:
            raise BombError()
    
    def flag_cell(self):
        self.flagged = True
    
