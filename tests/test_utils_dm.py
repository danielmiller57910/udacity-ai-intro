import utils_dm
import unittest
SAMPLE_GRID = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
class TestDMUtils(unittest.TestCase):

    def test_get_grid_columns_and_rows(self):
        grid_cols, grid_rows = utils_dm.get_grid_columns(), utils_dm.get_grid_rows()
        self.assertEqual(grid_cols[0], 1)
        self.assertEqual(grid_cols[-1], 9)
        self.assertEqual(grid_rows[0], 'A')
        self.assertEqual(grid_rows[-1], 'I')
    
    def test_setup_grid(self):
        grid_board = utils_dm.grid_values(SAMPLE_GRID)
        self.assertEqual(grid_board['A1'], '.')
        self.assertEqual(grid_board['A3'], '3') 
        self.assertEqual(grid_board['I9'], '.')