# main.py
# Author: Asa LeHolland

# import numpy to handle array board
import numpy as np 




def npdisplay(board):
	"""
	Function to convert the provided puzzle to a numpy array, which is output as a square board
	"""
	print(np.matrix(board)) 



def is_placement_possible(y, x, n, board):
	"""
	Returns whether or not a number can be placed at a provided coordinate
	This function uses the following format: board[y][x] == is_placement_possible(n)?

	:param x: the provided x coordinate (the column number from left)
	:param y: the provided y coordinate (the row number from the top)
	:param n: the integer for which to test placement in that particular location
	:param board: the current sudoku board for which to test on
	"""

	# Iterate over all possible indices for the rows  
	for i in range(0, 9):

		# First check each cell in the provided row to see if the provided number is already present
		if board[y][i] == n:

			# If the provided number is found in the row, then it is not possible to place
			return False

		# Then check each cell in the provided column to see if the provided number is already present 
		if board[i][x] == n:

			# If the provided number is found in the column, then it is not possible to place
			return False

	# Check within the current subsquare
	# First, determine which third of the rows the provided coordinates fall into
	subsquare_x = (x//3)*3 # For example, if x=8, (x//3)*3 = 6, which is the first index of the 3rd horizontal subsquare of the board
	subsquare_y = (y//3)*3 # For example, if y=2, (y//3)*3 = 0, which is the first index of the 1st vertical subsquare of the board

	# Once we know which subsquare we are placing into, we can iterate over each cell in that subsquare.
	# This is done by adding 0, 1 or 2 to the first index of both the vertical and horizontal coordinates of that subsquare  
	for i in range(3):
		for j in range(3):
			if board[subsquare_y+i][subsquare_x+j] == n:

				# If a cell within the subsquare contains the provided number, then it is not possible to place
				return False

	# If we have reached here, then the provided number n is not present in the row, column, or subsquare. 
	# Return True, since it is possible to place the number at these coordinates
	return True

	
def find_empty_location(board, coordinates):
	"""
	Finds the next empty location on the Sudoku Board
	:param board: 9x9 array of arrays representing a sudoku board
	:param coordinates: temp coordinates of a row and column value that will be mutated to store the coordinates of the empty location
	:return: True if empty location is found, False if no remaining cells are found. 
	"""

	# iterate over each row (y values)
	for y_i in range(9):

		# iterate over each column (x values)
		for x_j in range(9):

			# check each cell at the provided indices and see if it is 0 (or not solved yet)
			if board[y_i][x_j] == 0:

				# if a digit has not been placed in a cell, save the coordinates of that cell and return True 
				# mutate the provided coordinates
				coordinates[0]= y_i
				coordinates[1]= x_j
				return True

	# If there are no remaining empty cells, we return False
	return False
	

def solve_sudoku(board_to_solve):
	"""
	Provided an unfinished sudoku puzzle, attempt to solve the puzzle by using recursion and backtracking
	:param board_to_solve: a 9x9 array of arrays representing a Sudoku puzzle board
	:return: True if a valid solution is found or False if no valid solution was found
	"""
		
	# define the current coordinates of the Sudoku cell we are examining. 
	# Start in the upper left corner 
	current_coords = [0, 0]

	# Check if all cells have been filled
	if not find_empty_location(board=board_to_solve, coordinates=current_coords):

		# If so, we have solved the puzzle. Return True
		return True

	# Assign row and column values using the provided coordinates 
	[row, col] = current_coords
	
	# If the cell is not solved yet, attempt to solve it using each possible digit
	for digit in range(1, 10):
		
		# Check if it is possible to place the digit there
		if is_placement_possible(y=row, x=col, n=digit, board=board_to_solve):
			
			# If the digit is possible to place, place it
			board_to_solve[row][col] = digit
			 
			# Then, check to see if placing this final digit solves the puzzle.
			if solve_sudoku(board_to_solve=board_to_solve):

				# If so, return True stating we have found the solution
				return True
				
			# Otherwise, take away the placed digit and continue the iteration
			board_to_solve[row][col] = 0
			
	# If a dead end is reached (no possible digits are placeable), then it means 
	# that we we made a mistake earlier in our placements 
	# (in which case, returning False will backtrack and we can replace the value with a 0)
	# OR there is no valid solution to this puzzle (it is impossible)
	return False


def is_valid_sudoku(board_to_test):
	"""
	Provided a sudoku board, determine if it is a valid, complete solution.
	:param board_to_test: a 9x9 array representing a sudoku board for which we want to determine validity
	:return: A dictionary containing the following key value pairs:
		'is_valid': True if the provided board is valid or False if the board is not valid
		'invalid_row': integer of the index of the first invalid row found
		'invalid_column': integer of the index of the first invalid column found
		'invalid_digit': the invalid digit placed at the invalid row and column
	"""

	# iterate over rows (y values)
	for row in range(9):
		# iterate over columns (x values)
		for col in range(9):

			# First, check that the cell at the current row and column is not empty
			if board_to_test[row][col] == 0:

				# If the cell is not filled, then the provided board is not complete. Therefore it is not valid.
				return {'is_valid': False, 'invalid_row': row, 'invalid_column': col, 'invalid_digit': 0}

			# Then, check the value of the cell.
			# Remove the value of the cell and store it as a temp variable.
			temp = board_to_test[row][col]
			board_to_test[row][col] = 0

			# Then attempt to put the same value back in the board
			if not is_placement_possible(y=row, x=col, n=temp, board=board_to_test):

				# If it is not possible to place this value in the board, then the provided board is not valid
				return {'is_valid': False, 'invalid_row': row, 'invalid_column': col, 'invalid_digit': temp}

	# If all cells are valid, then we can return True.
	# Return an empty coordinate set 
	return {'is_valid': True, 'invalid_row': None, 'invalid_column': None, 'invalid_digit': None}



def confirm_puzzle_is_solvable(puzzle):
	"""
	Solves and validates a 
	"""
	if not solve_sudoku(board_to_solve=puzzle):
		return "This particular Sudoku puzzle cannot be solved."

	validation = is_valid_sudoku(board_to_test=puzzle)

	if validation['is_valid']:
		return "At least one valid solution for the provided puzzle exists."

	else:
		return "Error! The provided puzzle is possible to solve, but a valid solution was not found."



def validate_user_submission(user_board):
	"""
	Solves and validates a user-provided board
	"""
	validation = is_valid_sudoku(board_to_test=user_board)

	if validation['is_valid']:
		return "The provided submission is valid! Nice work." 

	else:
		return f"""The provided submission is not valid. 
			The digit in Row {validation['invalid_row']}, Column {validation['invalid_row']} 
			cannot be {validation['invalid_digit']}.""" 