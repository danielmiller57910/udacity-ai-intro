from string import ascii_letters
import pdb
def grid_values(grid: str) -> dict:
    sudoku_board_dictionary = {}
    grid_rows, grid_columns = get_grid_rows(), get_grid_columns()
    grid_index = 0
    for row in grid_rows:
        for col in grid_columns:
           sudoku_board_dictionary[row+str(col)] = grid[grid_index]
           grid_index +=1
    
    return sudoku_board_dictionary

def get_grid_columns():
    return [i for i in range(1, 10)]

def get_grid_rows():
    return [ascii_letters[ascii_letters.index('A') + i] for i in range(0, 9)]

