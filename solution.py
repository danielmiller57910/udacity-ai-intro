from utils import *
from string import ascii_letters
import copy
import pdb
CHARACTER_LIST= "ABCDEFGHI"
NUMBER_LIST = "123456789"

def get_unique_board_set(associated_nodes):
    associated_nodes.build_set()
    return associated_nodes.return_unique_board_set()

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

def create_grid_columns():
    return [i for i in range(1, 10)]

def create_grid_rows():
    return [ascii_letters[ascii_letters.index('A') + i] for i in range(0, 9)]

def naked_queens():
    top_list, bottom_list = get_top_and_bottom_list([], [])
    return top_list, bottom_list

def get_top_and_bottom_list(top_list, bottom_list):
    for i in range(len(CHARACTER_LIST)):
        top_list.append(CHARACTER_LIST[i] + NUMBER_LIST[i])

    reversed_numbers = NUMBER_LIST[::-1]
    for i in range(len(CHARACTER_LIST)):
        bottom_list.append(CHARACTER_LIST[i] + reversed_numbers[i])
    return top_list, bottom_list

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

    LEFT_DIAGONAL_VALUES, RIGHT_DIAGONAL_VALUES = naked_queens()

    def __init__(self, board_position: str):
        self.board_position = board_position
        self.row_set = []
        self.col_set = []
        self.grid_set = []
        self.diagonal_set = []
    
    def build_set(self):
        row_pos, col_pos = self.board_position[0], self.board_position[-1]
        self.row_set = [row_pos + str(i) for i in range (1, 10)]
        self.col_set = [row + col_pos for row in create_grid_rows()]
        self.grid_set = self._build_grid_set(row_pos, col_pos)
        if self.board_position in self.LEFT_DIAGONAL_VALUES:
            self.diagonal_set.extend(self.LEFT_DIAGONAL_VALUES)
        if self.board_position in self.RIGHT_DIAGONAL_VALUES:
            self.diagonal_set.extend(self.RIGHT_DIAGONAL_VALUES)
    
    def _build_grid_set(self, row_pos, col_pos):

        row_start_pos, col_start_pos = self.ROW_START_DICT[row_pos], self.COL_START_DICT[int(col_pos)]
        grid_list = []
        for i in range(row_start_pos, row_start_pos + 3):
            for j in range(col_start_pos, col_start_pos + 3):
                current = chr(ord('@')+i) + str(j)
                grid_list.append(current)
        return grid_list
    
    def return_unique_board_set(self):
        unique_set = sorted(set(self.row_set + self.col_set + self.grid_set + self.diagonal_set))
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
        return ''.join([str(val) for val in self.ALLOWED_VALUES if val not in self.value_range])

def find_possible_twins(values):
    possible_twins = {}
    for k, v in values.items():
        if len(v) == 2:
            possible_twins[k] = v 
    return possible_twins

def find_unique_twins(possible_twins: dict) -> list:
    actual_twins = []
    for k, v in possible_twins.items():
        twin = dict(filter(lambda item: item[1] == v, possible_twins.items()))
        if len(twin.values()) == 2:
            twin = {"node_1": list(twin.keys())[0], "node_2": list(twin.keys())[-1], "value": list(twin.values())[0]}
            actual_twins.append(twin)
    return list({x['node_1']:x for x in actual_twins}.values())

def nodes_share_intersection(node_set):  
   return node_set['node_2'] in get_unique_board_set(AssociatedNodes(node_set['node_1']))

def identify_associated_nodes(node_set):
    grid_intersection = get_unique_board_set(AssociatedNodes(node_set['node_1'])) + get_unique_board_set(AssociatedNodes(node_set['node_2']))
    node_set['grid_intersection'] = set([i for i in grid_intersection if i != node_set['node_1'] and i != node_set['node_2']])
    return node_set

def naked_twins(values: dict) -> dict:
    possible_twins = find_possible_twins(values.copy())
    shared_values = find_unique_twins(possible_twins)
    peers = filter(nodes_share_intersection, shared_values)
    peers = map(identify_associated_nodes, peers)
    for peer in peers:
        print(peer)
        value = peer['value']
        for intersection in peer['grid_intersection']:
            values[intersection] = values[intersection].replace(value, "")
    
    return values
    

    
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """



def eliminate(grid: dict) -> dict:
    node_eliminator = NodeEliminator(grid)
    return node_eliminator.remove_completed_indexes_from_grid()

def only_choice(grid: dict) -> dict:
    only_choice = NodeOnlyChoice(grid)
    return only_choice.eliminate()

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def solved(values):
    diagonal_values = [str(i) for i in range(1, 10)]
    left_dag, right_dag = naked_queens()
    for k, v in values.items():
        if len(v) != 1:
            return False
    
    left_diagonal_values, right_diagonal_values = [values[k] for k in left_dag], [values[j] for j in right_dag]
    return sorted(left_diagonal_values) == diagonal_values and sorted(right_diagonal_values) == diagonal_values

def pick(grid):
    possible_keys = [{"key": k, "value": v} for k, v in grid.items() if len(v) != 1]
    return sorted(possible_keys, key=lambda i: len(i['value']))[0]['key']

def search(values):

    values = reduce_puzzle(values)
    if values is False: return False 
    
    if solved(values): return values
        
    current = pick(values)
    for value in values[current]:
        new_sudoku = copy.deepcopy(values)
        new_sudoku[current] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(values):
    sudoku_grid = grid_values(values)
    return search(sudoku_grid)

