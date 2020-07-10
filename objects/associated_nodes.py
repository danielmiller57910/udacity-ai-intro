from string import ascii_letters

def create_grid_columns():
    return [i for i in range(1, 10)]

def create_grid_rows():
    return [ascii_letters[ascii_letters.index('A') + i] for i in range(0, 9)]

from naked_queens import naked_queens
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