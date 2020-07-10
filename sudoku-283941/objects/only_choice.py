from objects.associated_nodes import AssociatedNodes

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


def get_unique_board_set(associated_nodes):
    associated_nodes.build_set()
    return associated_nodes.return_unique_board_set()