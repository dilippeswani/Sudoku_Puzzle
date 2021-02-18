import unittest
from sudoku_class import *


class sudoku_test(unittest.TestCase):

    def test_zero_values(self):
        puzzle = solve_sudoku(sudoku)
        result = puzzle.count_of_zeros(sudoku)
        self.assertEqual(result , 0)


if __name__ == '__main__':
    unittest.main()
