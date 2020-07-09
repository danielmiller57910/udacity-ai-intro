from utils import *
from string import ascii_letters
from objects.associated_nodes import AssociatedNodes
import pdb
import copy

def naked_twins(values):
    """Eliminate values using the naked twins strategy.

    The naked twins strategy says that if you have two or more unallocated boxes
    in a unit and there are only two digits that can go in those two boxes, then
    those two digits can be eliminated from the possible assignments of all other
    boxes in the same unit.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the naked twins eliminated from peers

    Notes
    -----
    Your solution can either process all pairs of naked twins from the input once,
    or it can continue processing pairs of naked twins until there are no such
    pairs remaining -- the project assistant test suite will accept either
    convention. However, it will not accept code that does not process all pairs
    of naked twins from the original input. (For example, if you start processing
    pairs of twins and eliminate another pair of twins before the second pair
    is processed then your code will fail the PA test suite.)

    The first convention is preferred for consistency with the other strategies,
    and because it is simpler (since the reduce_puzzle function already calls this
    strategy repeatedly).

    See Also
    --------
    Pseudocode for this algorithm on github:
    https://github.com/udacity/artificial-intelligence/blob/master/Projects/1_Sudoku/pseudocode.md
    """
    # TODO: Implement this function!
    raise NotImplementedError


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

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(copy.deepcopy(values))
        values = only_choice(copy.deepcopy(values))
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def solved(values):
    for k, v in values.items():
        if len(v) != 1:
            return False
    return True

def pick(grid):
    possible_keys = [{"key": k, "value": v} for k, v in grid.items() if len(v) != 1]
    return sorted(possible_keys, key=lambda i: len(i['value']))[0]['key']

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False 
    
    if solved(values): 
        return values
        
    current = pick(values)
    for value in values[current]:
        new_sudoku = copy.deepcopy(values)
        new_sudoku[current] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(values):
    return search(values)

if __name__ == "__main__":
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(grid2values(diag_sudoku_grid))
    result = solve(diag_sudoku_grid)
    display(result)

    try:
        import PySudoku
        PySudoku.play(grid2values(diag_sudoku_grid), result, history)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
