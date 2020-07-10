from objects.associated_nodes import AssociatedNodes

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


def get_unique_board_set(associated_nodes):
    associated_nodes.build_set()
    return associated_nodes.return_unique_board_set()