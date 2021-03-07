# filename: consoleSudokuUI.py
# author: Asa Holland



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

	{
	'puzzle_name': 'Easy Sudoku',
	'source:' 'https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html'
	'puzzle': [	[0,0,0, 2,6,0, 7,0,1],
				[6,8,0, 0,7,0, 0,9,0],
				[1,9,0, 0,0,4, 5,0,0],

				[8,2,0, 1,0,0, 0,4,0],
				[0,0,4, 6,0,2, 9,0,0],
				[0,5,0, 0,0,3, 0,2,8],

				[0,0,9, 3,0,0, 0,7,4],
				[0,4,0, 0,5,0, 0,3,6],
				[7,0,3, 0,1,8, 0,0,0]	]
	}, 

	{
	'puzzle_name': 'Impossible Sudoku',
	'source:' 'https://www.sudokudragon.com/unsolvable.htm'
	'puzzle': [	[0,0,0, 2,6,0, 7,0,1],
				[6,8,0, 0,7,0, 0,9,0],
				[1,9,0, 0,0,4, 5,0,0],

				[8,2,0, 1,0,0, 0,4,0],
				[0,0,4, 6,0,2, 9,0,0],
				[0,5,0, 0,0,3, 0,2,8],

				[0,0,9, 3,0,0, 0,7,4],
				[0,4,0, 0,5,0, 0,3,6],
				[7,0,3, 0,1,8, 0,0,0]	]
	}, 




}

def welcome():
	"""
	Welcomes the user to Console Sudoku.
	"""
	pass


def present_options():
	"""
	Present user with options
	"""
	# Allow user to open a random sudoku puzzle from library
	# Allow user to quit
	# Allow user to add a new sudoku puzzle to library
	# Allow user to delete existing sudoku puzzle from library
	pass


def open_puzzle(puzzle_serial_to_open):

	# Allow user to attempt to solve the puzzle

	# Allow user to view a solution

	# Allow user to quit and return to puzzle selection

	# Allow user to quit Console Sudoku


