from objects.empty_node import EmptyNode
from objects.associated_nodes import AssociatedNodes
from string import ascii_letters

def get_unique_board_set(associated_nodes):
    associated_nodes.build_set()
    return associated_nodes.return_unique_board_set()

def create_grid_columns():
    return [i for i in range(1, 10)]

def create_grid_rows():
    return [ascii_letters[ascii_letters.index('A') + i] for i in range(0, 9)]

def empty_grid_indexes(grid: dict) -> dict:
    return [index for index, value in grid.items() if value == '.']

def grid_values(grid: str) -> dict:
    sudoku_board_dictionary = {}
    grid_rows, grid_columns = create_grid_rows(), create_grid_columns()
    grid_index = 0
    for row in grid_rows:
        for col in grid_columns:
           sudoku_board_dictionary[row+str(col)] = grid[grid_index]
           grid_index +=1
    
    empty_indexes = empty_grid_indexes(sudoku_board_dictionary)
    for index in empty_indexes:
        empty_node = EmptyNode(
            index,
            get_unique_board_set(AssociatedNodes(index)), 
            sudoku_board_dictionary
        )
        sudoku_board_dictionary[empty_node.node] = empty_node.get_value_range()
    
    return sudoku_board_dictionary