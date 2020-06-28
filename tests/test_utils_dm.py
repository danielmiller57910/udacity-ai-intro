import utils_dm
import unittest
SAMPLE_GRID = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
class TestDMUtils(unittest.TestCase):

    def test_create_grid_columns_and_rows(self):
        grid_cols, grid_rows = utils_dm.create_grid_columns(), utils_dm.create_grid_rows()
        self.assertEqual(grid_cols[0], 1)
        self.assertEqual(grid_cols[-1], 9)
        self.assertEqual(grid_rows[0], 'A')
        self.assertEqual(grid_rows[-1], 'I')
    
    def test_setup_grid(self):
        grid_board = utils_dm.grid_values(SAMPLE_GRID)
        self.assertEqual(grid_board['A1'], '.')
        self.assertEqual(grid_board['A3'], '3') 
        self.assertEqual(grid_board['I9'], '.')
    
    def test_build_row_col_set(self):
        board_set = utils_dm.BoardSet('A5')
        board_set.build_set()
        self.assertEqual(board_set.row_set[1], 'A2')
        self.assertEqual(board_set.row_set[-1], 'A9')
        self.assertEqual(board_set.col_set[0], 'A5')
        self.assertEqual(board_set.col_set[-1], 'I5')

    def test_build_grid_set(self):
        board_set = utils_dm.BoardSet('I9')
        board_set.build_set()
        self.assertEqual(board_set.grid_set[0], 'G7') 
        self.assertEqual(board_set.grid_set[-1], 'I9') 