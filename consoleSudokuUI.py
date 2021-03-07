# filename: consoleSudokuUI.py
# author: Asa Holland

import random

puzzles = {

	{
	'puzzle_name': 'Very, Very Easy Sudoku',
	'source:' 'Asa Holland'
	'puzzle': [	[1,2,3, 5,4,7, 6,8,9],
				[4,5,6, 2,9,8, 1,3,7],
				[7,8,9, 3,6,1, 2,4,5],

				[5,4,7, 1,2,3, 8,9,6],
				[2,9,8, 4,0,6, 3,7,1],
				[3,6,1, 7,8,9, 4,5,2],

				[6,1,4, 8,7,5, 9,2,3],
				[8,3,5, 9,1,2, 7,6,4],
				[9,7,2, 6,3,4, 5,1,8]	]	
	}, 

	# {
	# 'puzzle_name': 'Easy Sudoku',
	# 'source:' 'https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html'
	# 'puzzle': [	[0,0,0, 2,6,0, 7,0,1],
	# 			[6,8,0, 0,7,0, 0,9,0],
	# 			[1,9,0, 0,0,4, 5,0,0],

	# 			[8,2,0, 1,0,0, 0,4,0],
	# 			[0,0,4, 6,0,2, 9,0,0],
	# 			[0,5,0, 0,0,3, 0,2,8],

	# 			[0,0,9, 3,0,0, 0,7,4],
	# 			[0,4,0, 0,5,0, 0,3,6],
	# 			[7,0,3, 0,1,8, 0,0,0]	]
	# }, 

	# {
	# 'puzzle_name': 'Impossible Sudoku',
	# 'source:' 'https://www.sudokudragon.com/unsolvable.htm'
	# 'puzzle': [	[0,0,0, 2,6,0, 7,0,1],
	# 			[6,8,0, 0,7,0, 0,9,0],
	# 			[1,9,0, 0,0,4, 5,0,0],

	# 			[8,2,0, 1,0,0, 0,4,0],
	# 			[0,0,4, 6,0,2, 9,0,0],
	# 			[0,5,0, 0,0,3, 0,2,8],

	# 			[0,0,9, 3,0,0, 0,7,4],
	# 			[0,4,0, 0,5,0, 0,3,6],
	# 			[7,0,3, 0,1,8, 0,0,0]	]
	# }, 
}

def welcome():
	"""
	Welcomes the user to Console Sudoku.
	"""
	print('Welcome to Console Sudoku!')


def describe_sudoku():


def load_random_sudoku():


def present_options():
	"""
	Present user with options
	"""

	valid_selections = {}

	# Allow user to read a description about Sudoku
	option_1 = 'Read a short description about Sudoku.'
	valid_selections[1] = describe_sudoku

	# Allow user to open a random sudoku puzzle from library
	option_2 = 'Load a random Sudoku puzzle from the Puzzle Library.'
	valid_selections[2] = load_random_sudoku

	# # Allow user to view all sudoku puzzles in library
	# option_3 = 'Select a specific Sudoku puzzle from the Puzzle Library.'
	# valid_selections[1] = describe_sudoku

	# # Allow user to add a new sudoku puzzle to library
	# option_4 = 'Add a new Sudoku puzzle to Puzzle Library.'
	# valid_selections[1] = describe_sudoku

	# # Allow user to delete existing sudoku puzzle from library
	# option_5 = 'Delete an existing Sudoku puzzle from the Puzzle Library.'
	# valid_selections[1] = describe_sudoku

		# 3. {option_3}
		# 4. {option_4}
		# 5. {option_5}


	user_selection = input(f"""

		Please enter one of the following options:
		1. {option_1}
		2. {option_2}

		Or enter 'Q' to quite Console Sudoku.
		""")

	running = True

	while running:

		if user_selection not in valid_selections:
			print("Error, please select one of the provided options or enter 'Q' to quit Console Sudoku.")




def open_puzzle(puzzle_serial_to_open):

	# Allow user to attempt to solve the puzzle

	# Allow user to view a solution

	# Allow user to quit and return to puzzle selection

	# Allow user to quit Console Sudoku
	pass


def user_solve(puzzle_for_user_to_solve):

	# Allow the user to move the 'cursor'

	# Allow the user to set the number in a cell

	# Allow the user to submit a solution

	# Allow the user to ask if the puzzle is possible

	# Allow the user to quit, returning them to puzzle selection

	# Allow the user to quite Console Sudoku
	pass


# when run as a script, run the console sudoku interface
if __name__ == '__main__':

	welcome()

	present_options()


