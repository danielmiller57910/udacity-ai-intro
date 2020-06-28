import utils_dm
import unittest

class TestDMUtils(unittest.TestCase):

    def test_get_grid_columns_and_rows(self):
        grid_cols, grid_rows = utils_dm.get_grid_columns(), utils_dm.get_grid_rows()
        self.assertEqual(grid_cols[0], 1)
        self.assertEqual(grid_cols[-1], 9)
        self.assertEqual(grid_rows[0], 'A')
        self.assertEqual(grid_rows[-1], 'J')