from board_set import AssociatedNodes
import submission_file
import unittest
SAMPLE_GRID = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
GRID_FOR_ELIMINATION = {'A1': '123456789', 'A2': '123456789', 'A3': '3', 'A4': '123456789', 'A5': '2', 'A6': '123456789', 'A7': '6', 'A8': '123456789', 'A9': '123456789', 'B1': '9', 'B2': '123456789', 'B3': '123456789', 'B4': '3', 'B5': '123456789', 'B6': '5', 'B7': '123456789', 'B8': '123456789', 'B9': '1', 'C1': '123456789', 'C2': '123456789', 'C3': '1', 'C4': '8', 'C5': '123456789', 'C6': '6', 'C7': '4', 'C8': '123456789', 'C9': '123456789', 'D1': '123456789', 'D2': '123456789', 'D3': '8', 'D4': '1', 'D5': '123456789', 'D6': '2', 'D7': '9', 'D8': '123456789', 'D9': '123456789', 'E1': '7', 'E2': '123456789', 'E3': '123456789', 'E4': '123456789', 'E5': '123456789', 'E6': '123456789', 'E7': '123456789', 'E8': '123456789', 'E9': '8', 'F1': '123456789', 'F2': '123456789', 'F3': '6', 'F4': '7', 'F5': '123456789', 'F6': '8', 'F7': '2', 'F8': '123456789', 'F9': '123456789', 'G1': '123456789', 'G2': '123456789', 'G3': '2', 'G4': '6', 'G5': '123456789', 'G6': '9', 'G7': '5', 'G8': '123456789', 'G9': '123456789', 'H1': '8', 'H2': '123456789', 'H3': '123456789', 'H4': '2', 'H5': '123456789', 'H6': '3', 'H7': '123456789', 'H8': '123456789', 'H9': '9', 'I1': '123456789', 'I2': '123456789', 'I3': '5', 'I4': '123456789', 'I5': '1', 'I6': '123456789', 'I7': '3', 'I8': '123456789', 'I9': '123456789'}

class TestDMUtils(unittest.TestCase):

    def test_create_grid_columns_and_rows(self):
        grid_cols, grid_rows = submission_file.create_grid_columns(), submission_file.create_grid_rows()
        self.assertEqual(grid_cols[0], 1)
        self.assertEqual(grid_cols[-1], 9)
        self.assertEqual(grid_rows[0], 'A')
        self.assertEqual(grid_rows[-1], 'I')
    
    def test_build_row_col_set(self):
        board_set = AssociatedNodes('A5')
        board_set.build_set()
        self.assertEqual(board_set.row_set[1], 'A2')
        self.assertEqual(board_set.row_set[-1], 'A9')
        self.assertEqual(board_set.col_set[0], 'A5')
        self.assertEqual(board_set.col_set[-1], 'I5')

    def test_build_grid_set(self):
        board_set = AssociatedNodes('I9')
        board_set.build_set()
        self.assertEqual(board_set.grid_set[0], 'G7') 
        self.assertEqual(board_set.grid_set[-1], 'I9') 
    
    def test_empty_index(self):
        sample_dict = {"A1": ".", "A2": "3", "A3": "."}
        self.assertEqual(submission_file.empty_grid_indexes(sample_dict), ["A1", "A3"])
    
    def test_grid_values(self):
        sudoku_board_dictionary = submission_file.grid_values(SAMPLE_GRID)
        eliminator = submission_file.NodeEliminator(sudoku_board_dictionary)
        eliminator.remove_completed_indexes_from_grid()
        for node in eliminator.completed_nodes:
            for k in node['associated_nodes']:
                print(f' {node["index"]}, {node["value"]}, {eliminator.grid[k]}')
                print(str(node["value"]) == eliminator.grid[k])

