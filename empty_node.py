import pdb

class EmptyNode:
    
    ALLOWED_VALUES = [i for i in range(1, 10)]

    def __init__(self, node: str, associated_indexes: list, grid: dict):
        self.node = node
        self.associated_indexes = associated_indexes
        self.grid = grid
        self.value_range = []
        self.legal_positions = None
    
    def identify_filled_values(self):
        for index in self.associated_indexes:
            print(index, self.grid[index])
