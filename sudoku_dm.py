import pdb
from string import ascii_letters
from board_set import AssociatedNodes

def grid_values(grid: str) -> dict:
    sudoku_board_dictionary = {}
    grid_rows, grid_columns = create_grid_rows(), create_grid_columns()
    grid_index = 0
    for row in grid_rows:
        for col in grid_columns:
           sudoku_board_dictionary[row+str(col)] = grid[grid_index]
           grid_index +=1
    
    empty_indexes = empty_grid_indexes(sudoku_board_dictionary)
    return sudoku_board_dictionary

def create_grid_columns():
    return [i for i in range(1, 10)]

def create_grid_rows():
    return [ascii_letters[ascii_letters.index('A') + i] for i in range(0, 9)]

def empty_grid_indexes(grid: dict) -> dict:
    return [index for index, value in grid.items() if value == '.']