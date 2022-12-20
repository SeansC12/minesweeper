import random
import settings

# TODO: Add class method for win-lose
# TODO: Code for instantiating the game
# TODO: Implement solver for 

class Cell:
    all = [] # All cells in the board
    row_count = 1 # To be changed
    cell_count = (settings.ROW_COUNT) ** 2
    def __init__(self, row, row_index, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.flagged = False
        self.row = row # Row in board, from 0 to n
        self.row_index = row_index # Triangle number in the row, from left to right

        Cell.all.append(self)

    def get_cell_by_axis(self, row, index): # To get a cell by its row and its row index
        for cell in Cell.all:
            if cell.row == row and cell.row_index == index: # Searches all cells for cell with specific row and index
                return cell

    
    @property
    def surrounded_cells_mines_length(self): # Cell-mine adjacency number
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter
    
    @property
    def surrounded_cells(self): # Method for getting cell neighbours
        within_row_index = [-2, -1, 0, 1, 2] # Index set to iterate over neighbours in the same row
        across_row_index = [-1, 0, 1] # Index set to iterate over neighbours below and above the row
        cells = [] # List of neighbours
        for x in within_row_index:
            for y in across_row_index:
                cells.append(self.get_cell_by_axis(self.row_index - x, self.row - y)) # Appends list of neighbours with coordinates (row, row_index) of neighbours

        cells = [cell for cell in cells if cell is not None] # Ejects cells that do not exist
        return cells
    
    def left_click_actions(self, event): 
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell() # Revealing all neighbours if cell-mine adjacency == 0
            
            if Cell.cell_count == settings.MINES_COUNT: # Invoke win message 
                print("Win")
            

    def show_cell(self): # Graphical representation when cell is revealed
        if not self.is_opened: # self.is_opened turns to true, meaning the cell is revealed
            pass

    def show_mine(self): # Lose situation, clicked on mine
        print("Clicked on mine")

    def right_click_actions(self): # Flagging cells, user input
        if not self.flagged:
            self.flagged = True
        else: 
            self.flagged = False
    
    @staticmethod
    def randomise_mines(): # Choosing the set of mines from the set of cells
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
    
    def __repr__(self):
        return f"Cell({self.row_index}, {self.row})" # Returns the position of the cell instance when the instance is called
    
