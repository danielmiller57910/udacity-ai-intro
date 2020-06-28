from string import ascii_letters
import pdb
import math

def grid_values(grid: str) -> dict:
    sudoku_board_dictionary = {}
    grid_rows, grid_columns = create_grid_rows(), create_grid_columns()
    grid_index = 0
    for row in grid_rows:
        for col in grid_columns:
           sudoku_board_dictionary[row+str(col)] = grid[grid_index]
           grid_index +=1
    
    return sudoku_board_dictionary

def create_grid_columns():
    return [i for i in range(1, 10)]

def create_grid_rows():
    return [ascii_letters[ascii_letters.index('A') + i] for i in range(0, 9)]


class BoardSet:

    ROW_START_DICT = {
        'A': 1,
        'B': 1,
        'C': 1,
        'D': 4,
        'E': 4,
        'F': 4,
        'G': 7,
        'H': 7,
        'I': 7
    }

    COL_START_DICT = {
        1: 1,
        2: 1,
        3: 1,
        4: 4,
        5: 4,
        6: 4,
        7: 7,
        8: 7,
        9: 7
    }

    def __init__(self, board_position: str):
        self.board_position = board_position
        self.row_set = []
        self.col_set = []
        self.grid_set = []
    
    def build_set(self):
        row_pos, col_pos = self.board_position[0], self.board_position[-1]
        self.row_set = [f'{row_pos}{i}' for i in range (1, 10)]
        self.col_set = [f'{col}{col_pos}' for col in create_grid_rows()]
        self.grid_set = self._build_grid_set(row_pos, col_pos)
    
    def _build_grid_set(self, row_pos, col_pos):

        row_start_pos, col_start_pos = self.ROW_START_DICT[row_pos], self.COL_START_DICT[int(col_pos)]
        grid_list = []
        
        for i in range(row_start_pos, row_start_pos + 3):
            row = chr(ord('@')+i) 
            for j in range(col_start_pos, col_start_pos + 3):
               grid_list.extend(f'{row}{j}')

        return grid_list 
        


        
