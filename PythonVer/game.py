from cell import Cell
import settings
import sys

def row_max(x): # Function that calculates the number of cells in each row
    return (2*x + 1)

def initialiseBoard(): # Initialise board arrangement
    for x in range(settings.ROW_COUNT): # settings.ROW_COUNT = 5
        for y in range(row_max(x)):
            c = Cell(x, y) # Initialises a cell for each (x, y)
'''
Plan to run game each iteration, need to include solver function from solver.py
'''
def game():
    # Initialise game state
    Cell.game_is_ongoing = True
    Cell.isWin = False
    Cell.isLose = False
    iterations = settings.ITERATIONS
    clicks = 0

    while Cell.game_is_ongoing == True:
        if clicks == 1:
            Cell.randomise_mines()
        if Cell.isWin == True:
            Cell.currentIteration += 1
            game_is_ongoing = False
        elif Cell.isLose == False:
            Cell.currentIteration += 1
            game_is_ongoing = False
    
    while Cell.currentIteration <= 5:
        game()
    else:
        sys.exit()
        '''
        code that calculates statistics for single instance of iterations and
        exports statistics to some kind of data file using numpy or something,
        idk.
        '''

        
        
        
        

