from utils import *
from string import ascii_letters
from objects.associated_nodes import AssociatedNodes
from objects.eliminate import NodeEliminator
from objects.only_choice import NodeOnlyChoice
from objects.empty_node import EmptyNode
from objects.grid_values import grid_values
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
    sudoku_grid = grid_values(values)
    return search(sudoku_grid)

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
