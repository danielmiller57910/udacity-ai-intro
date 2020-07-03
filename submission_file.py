from utils import *
from string import ascii_letters
import pdb
import copy

def create_grid_columns():
    return [i for i in range(1, 10)]

def create_grid_rows():
    return [ascii_letters[ascii_letters.index('A') + i] for i in range(0, 9)]

def empty_grid_indexes(grid: dict) -> dict:
    return [index for index, value in grid.items() if value == '.']

def get_unique_board_set(associated_nodes):
    associated_nodes.build_set()
    return associated_nodes.return_unique_board_set()

class AssociatedNodes:

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
        self.row_set = [row_pos + str(i) for i in range (1, 10)]
        self.col_set = [row + col_pos for row in create_grid_rows()]
        self.grid_set = self._build_grid_set(row_pos, col_pos)
    
    def _build_grid_set(self, row_pos, col_pos):

        row_start_pos, col_start_pos = self.ROW_START_DICT[row_pos], self.COL_START_DICT[int(col_pos)]
        grid_list = []
        for i in range(row_start_pos, row_start_pos + 3):
            for j in range(col_start_pos, col_start_pos + 3):
                current = chr(ord('@')+i) + str(j)
                grid_list.append(current)
        return grid_list
    
    def return_unique_board_set(self):
        unique_set = sorted(set(self.row_set + self.col_set + self.grid_set))
        return [el for el in unique_set if el != self.board_position]

class EmptyNode:
    
    ALLOWED_VALUES = [i for i in range(1, 10)]

    def __init__(self, node: str, associated_indexes: list, grid: dict):
        self.node = node
        self.associated_indexes = associated_indexes
        self.grid = grid
        self.value_range = self._identify_filled_values()
    
    def _identify_filled_values(self):
        associated_values = [self.grid[i] for i in self.associated_indexes]
        return [int(val) for val in associated_values if val != '.']
    
    def get_value_range(self):
        return ''.join([str(val) for val in self.ALLOWED_VALUES])

class NodeEliminator:
    def __init__(self, grid: dict) -> dict:
        self.grid = grid
        self.completed_nodes = self._find_completed_nodes()

    def remove_completed_indexes_from_grid(self):
        for node in self.completed_nodes:
            value_for_elimination = node["value"]
            for index in node["associated_nodes"]:
                self.grid[index] = self._remove_value(value_for_elimination, self.grid[index])
        return self.grid
    
    def _find_completed_nodes(self):
        completed_nodes = []
        for k, v in self.grid.items():
            if len(v) == 1:
                completed_nodes.append({
                    "index": k, 
                    "value": v, 
                    "associated_nodes": get_unique_board_set(AssociatedNodes(k))
               })
        return completed_nodes
    
    def _remove_value(self, value_for_elimination, options_string):
        return options_string.replace(str(value_for_elimination), "")
        

class NodeOnlyChoice:
    def __init__(self, grid: dict) -> dict:
        self.grid = grid
        self.incomplete_nodes = self._find_incomplete_nodes()

    def eliminate(self):
        print("\n")
        for i in self.incomplete_nodes:
            current_index, current_value = i['index'], i['value']
            for j in i["associated_nodes"]:
                if len(self.grid[j]) == 1:
                    impossible_value = str(self.grid[j])
                    if impossible_value in current_value:
                        current_value = current_value.replace(impossible_value, "")
                    self.grid[current_index] = current_value
        return self.grid
    
    def _find_incomplete_nodes(self):
        incomplete_nodes = []
        for k, v in self.grid.items():
            if len(v) > 1:
                incomplete_nodes.append({
                    "index": k, 
                    "value": v, 
                    "associated_nodes": get_unique_board_set(AssociatedNodes(k))
               })
        return incomplete_nodes


def eliminate(grid: dict) -> dict:
    node_eliminator = NodeEliminator(grid)
    return node_eliminator.remove_completed_indexes_from_grid()

def only_choice(grid: dict) -> dict:
    only_choice = NodeOnlyChoice(grid)
    return only_choice.eliminate()

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