# filename: consoleSudokuUI.py
# author: Asa Holland



puzzles = {

	{
	'puzzle_name': 'Impossible Sudoku',
	'source:' 'https://www.sudokudragon.com/unsolvable.htm'
	'puzzle': [	[4,6,7, 9,2,1, 3,5,8],
				[8,9,5, 4,7,3, 2,6,1],
				[2,3,1, 8,6,5, 7,4,9],

				[5,1,3, 6,9,8, 4,2,7],
				[9,2,8, 7,0,4, 6,1,3],
				[7,4,6, 1,3,2, 9,8,5],

				[3,5,4, 2,8,7, 1,9,6],
				[0,0,0, 0,0,0, 0,0,0],
				[0,0,0, 0,0,0, 0,0,0]	]
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


