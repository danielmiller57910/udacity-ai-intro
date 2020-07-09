import unittest
from naked_queens import naked_queens
class TestNakedQueens(unittest.TestCase):
    def test_naked_queens(self):
        print(naked_queens())