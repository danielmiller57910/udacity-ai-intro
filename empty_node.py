import pdb

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

