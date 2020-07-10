from utils import *
from string import ascii_letters
from objects.associated_nodes import AssociatedNodes
from objects.eliminate import NodeEliminator
from objects.only_choice import NodeOnlyChoice
from objects.empty_node import EmptyNode
from objects.grid_values import grid_values
from naked_queens import naked_queens
import pdb
import copy

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find boxes with 2 entries
    candidates = [box for box in values.keys() if len(values[box]) == 2]

    # Collect boxes that have the same elements
    twins = [[box1,box2] for box1 in candidates for box2 in peers[box1] if set(values[box1]) == set(values[box2])]

    for b1,b2 in twins:
        print(b1, b2, values[b1])

    for box1, box2 in twins:

        peers1 = set(peers[box1])
        peers2 = set(peers[box2])

        peers_int = peers1.intersection(peers2)

        # delete the two digits from all common peers
        for peer_box in peers_int:
            for rm_val in values[box1]:
                values = assign_value(values, peer_box, values[peer_box].replace(rm_val,''))

    return values

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
