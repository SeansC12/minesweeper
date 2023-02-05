import numpy as np
import random
from cell import Cell
import settings

class BombError(Exception):
    def __init__(self, message='You just hit a bomb'):
        # Call the base class constructor with the parameters it needs
        super(BombError, self).__init__(message) 

# write a minesweeper solver in python

