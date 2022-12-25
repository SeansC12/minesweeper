from cell import Cell
import settings
import game
import random
from typing import List
import numpy as np

'''
1. Run click
2. Get board state
3. Assign variables
4. Solve system of equations
5. Repeat
'''

def getBoardState(cellAll: List[Cell]):
    known = []
    for cell in cellAll:
        if cell.is_opened == True:
            known.append(cell)
    return known

def algo():

    known = getBoardState(Cell.all)

    all_neighbour_unknown = set([])

    coefficient_map = {}

    coefficient_set = []

    result_vector = []

    for cell in known:
        coefficient_map[cell] = []
        for neighbour in cell.surrounded_cells:
            if neighbour.is_opened == False: 
                all_neighbour_unknown.add(neighbour)

        for ref in all_neighbour_unknown:
            if ref in cell.surrounded_cells:
                coefficient_map[cell].append(1) # Add coefficient if the unknown is in the cell neighbour unknowns
            elif ref not in cell.surrounded_cells:
                coefficient_map[cell].append(0) # No coefficient if not
        
    for boundary in coefficient_map:
        result_vector.append(boundary.surrounded_mines_length)
        coefficient_set.append(coefficient_map[boundary])
    
    return np.linalg.solve(np.array(coefficient_set), np.array(result_vector))
 
def solver():
    game.initialiseBoard()
    random.choice(Cell.all).left_click_actions()

    while Cell.game_is_ongoing:
        pass # Incomplete



    

solver()