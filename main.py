# main.py
# Author: Asa LeHolland


import numpy as np 



# method to convert the provided puzzle to a numpy array, which is output as a square board
def npdisplay(board):
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



def solve(board_to_solve, solved=False):

	# iterate over each row (y values)
	for y_i in range(9):

		# iterate over each column (x values)
		for x_j in range(9):

			# check each cell at the provided indices and see if it is 0 (or not solved yet)  
			if board_to_solve[y_i][x_j] == 0:

				# If the cell is not solved yet, attempt to solve it using each possible value
				for val in range(1, 10):

					# Check if it is possible to place the value there
					if is_placement_possible(y=y_i, x=x_j, n=val, board=board_to_solve):

						# If the value is possible to place, place it
						board_to_solve[y_i][x_j] = val

						# Recursively solve the board using the placed value
						if not solve(board_to_solve)[1]:

							# If the above recursive step fails, we return here.
							# In this case, the value we placed is not correct. We need to check another value.
							# We reset the board at that position, since this placement was incorrect.
							board_to_solve[y_i][x_j] = 0

				# If we reach here there are two possibilities
				# 1) If we are still inside the board but have run out of options to place another number
				# This means we made a mistake earlier in the placement
				print('y_i', y_i, 'x_j', x_j, 'val', val)
				return (board_to_solve, False)

	# If we reach here, we have iterated over all cells in the board
	# We have also filled all cells in the board.
	return (board_to_solve, True)



