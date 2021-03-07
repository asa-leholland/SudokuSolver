# test.py
# Author: Asa LeHolland
import unittest
import main as main_sudoku

# Puzzle Source: https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html
puzzle = [
[0,0,0, 2,6,0, 7,0,1],
[6,8,0, 0,7,0, 0,9,0],
[1,9,0, 0,0,4, 5,0,0],

[8,2,0, 1,0,0, 0,4,0],
[0,0,4, 6,0,2, 9,0,0],
[0,5,0, 0,0,3, 0,2,8],

[0,0,9, 3,0,0, 0,7,4],
[0,4,0, 0,5,0, 0,3,6],
[7,0,3, 0,1,8, 0,0,0]
]

# Solution Source: https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html
solution = [
[4,3,5, 2,6,9, 7,8,1],
[6,8,2, 5,7,1, 4,9,3],
[1,9,7, 8,3,4, 5,6,2],

[8,2,6, 1,9,5, 3,4,7],
[3,7,4, 6,8,2, 9,1,5],
[9,5,1, 7,4,3, 6,2,8],

[5,1,9, 3,2,6, 8,7,4],
[2,4,8, 9,5,7, 1,3,6],
[7,6,3, 4,1,8, 2,5,9]
]


# Impossible Puzzle
# Source: https://www.sudokudragon.com/unsolvable.htm
impossible_puzzle = [
[5,1,6, 8,4,9, 7,3,2],
[3,0,7, 6,0,5, 0,0,0],
[8,0,9, 7,0,0, 0,5,6],

[1,3,5, 0,6,0, 9,0,7],
[4,7,2, 5,9,1, 0,0,6],
[9,6,8, 3,7,0, 0,5,0],

[2,5,3, 1,8,6, 0,7,4],
[6,8,4, 2,0,7, 5,0,0],
[7,9,1, 0,5,0, 6,0,8]
]


# Blank Puzzle
blank_puzzle = [
[0,0,0, 0,0,0, 0,0,0],
[0,0,0, 0,0,0, 0,0,0],
[0,0,0, 0,0,0, 0,0,0],

[0,0,0, 0,0,0, 0,0,0],
[0,0,0, 0,0,0, 0,0,0],
[0,0,0, 0,0,0, 0,0,0],

[0,0,0, 0,0,0, 0,0,0],
[0,0,0, 0,0,0, 0,0,0],
[0,0,0, 0,0,0, 0,0,0]
]

# # Puzzle with Multiple soltutions
# # Source: https://www.sudokudragon.com/unsolvable.htm
# blank_puzzle = [
# [0,0,0, 0,0,0, 0,0,0],
# [0,0,0, 0,0,0, 0,0,0],
# [0,0,0, 0,0,0, 0,0,0],

# [0,0,0, 0,0,0, 0,0,0],
# [0,0,0, 0,0,0, 0,0,0],
# [0,0,0, 0,0,0, 0,0,0],

# [0,0,0, 0,0,0, 0,0,0],
# [0,0,0, 0,0,0, 0,0,0],
# [0,0,0, 0,0,0, 0,0,0]
# ]



class SudokuTestMethods(unittest.TestCase):

	def test_valid_placement(self):
		# Test that is_placement_possible() returns valid input for a Valid placement
		self.assertEqual(main_sudoku.is_placement_possible(y=0, x=0, n=3, board=puzzle), True)

	def test_invalid_row_placement(self):
		# Test that is_placement_possible() returns valid input for a non-valid placement in the same row
		self.assertEqual(main_sudoku.is_placement_possible(y=0, x=0, n=2, board=puzzle), False)

	def test_invalid_column_placement(self):
		# Test that is_placement_possible() returns valid input for a non-valid placement in the same column
		self.assertEqual(main_sudoku.is_placement_possible(y=0, x=0, n=8, board=puzzle), False)

	def test_invalid_subsquare_placement(self):
		# Test that is_placement_possible() returns valid input for a non-valid placement in the same subsquare
		self.assertEqual(main_sudoku.is_placement_possible(y=0, x=0, n=9, board=puzzle), False)

	def test_valid_solving(self):
		# Test that solve_sudoku() correctly solves a puzzle when compared to the actual solution
		attempt = puzzle
		main_sudoku.solve_sudoku(board_to_solve=attempt)
		self.assertEqual(attempt, solution)

	def test_impossible_solving(self):
		# Test that an impossible sudokue puzzle correctly returns False when attempted to solve
		attempt = impossible_puzzle
		self.assertEqual(main_sudoku.solve_sudoku(board_to_solve=attempt), False)

	def test_solved_solving(self):
		# Test that an already solved sudoku puzzle correctly returns True when attempted to solve
		attempt = solution
		self.assertEqual(main_sudoku.solve_sudoku(board_to_solve=attempt), True)

	def test_blank_solving(self):
		# Test that solution can be obtained from a fully blank sudoku board when attempted to solve
		attempt = blank_puzzle
		self.assertEqual(main_sudoku.solve_sudoku(board_to_solve=attempt), True)

	def test_validate_valid_board(self):
		# Test that a valid board proudces the correct result
		attempt = solution
		actual_result = main_sudoku.is_valid_sudoku(board_to_test=attempt)['is_valid']
		expected_result = True
		self.assertEqual(actual_result, expected_result)

	

# When run as a script, run the test cases
if __name__ == '__main__':
	unittest.main()