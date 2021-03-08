# filename: consoleSudokuUI.py
# author: Asa Holland

import random
import time

import re

import main as main_sudoku

puzzles = [

	{
	'puzzle_name': 'Very, Very Easy Sudoku',
	'source': 'Asa Holland',
	'puzzle': [	[1,2,3, 5,4,7, 6,8,9],
				[4,5,6, 2,9,8, 1,3,7],
				[7,8,9, 3,6,1, 2,4,5],

				[5,4,7, 1,2,3, 8,9,6],
				[2,9,8, 0,5,6, 3,7,1],
				[3,6,1, 7,8,9, 4,5,2],

				[6,1,4, 8,7,5, 9,2,3],
				[8,3,5, 9,1,2, 7,6,4],
				[9,7,2, 6,3,4, 5,1,8]	]	
	}, 

	# {
	# 'puzzle_name': 'Easy Sudoku',
	# 'source': 'https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html',
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
	# 'source': 'https://www.sudokudragon.com/unsolvable.htm',
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
]

def welcome():
	"""
	Welcomes the user to Console Sudoku.
	"""
	print("""
		Welcome to Console Sudoku!""")


def describe_sudoku():
	print('Sudoku is')

	time.sleep(3)

	return True


def confirm_solvable(board):
	print('\nChecking to see if the provided puzzle has a solution...')
	time.sleep(2)
	board_copy = board.copy()
	main_sudoku.confirm_puzzle_is_solvable(board_copy)
	time.sleep(1)
	return True


def generate_solution(board):
	print('\nChecking for a solution...')
	time.sleep(2)
	board_copy = list(board)
	if main_sudoku.solve_sudoku(board_to_solve=board_copy):

		print('\nOne valid solution to this Sudoku puzzle is as follows:')
		main_sudoku.npdisplay(board_copy)
	else:
		print('There is no valid solution for this puzzle.')
	time.sleep(1)
	return True

def user_place(current_board, blank_board):
	"""
	Allows a user to place a new number on the current version of the currently opened Sudoku board
	:param current_board: The current 9x9 array of the user's submission
	:param blank_board: The original 9x9 array for the user's puzzle, prior to any edits (not utilized by this function)
	"""
	user_input = input("Please enter the Row, Column, Value you would like to place: ")
	time.sleep(1)

	# Check if the user input is valid
	is_valid_input = bool(re.match(r"^[0-8], [0-8], [1-9]$", user_input))
	if not is_valid_input:
		print("""Invalid entry. To enter 2 in Row 3, Column 4, enter '2, 3, 4'.""")
		return False

	# Parse the user provided input
	[user_row, user_column, user_value] = [int(digit) for digit in user_input.split(', ')]

	# Check if the user input would change an original cell
	if blank_board[user_row][user_column] != 0:
		print("""Invalid placement. You can't change cells from the original provided puzzle.""")
		return False

	current_board[user_row][user_column] = user_value
	print(f"""Valid placement. You have placed a {user_value} in Row {user_row}, Column {user_column}.""")
	main_sudoku.npdisplay(current_board)
	return True


def user_submit(current_board, blank_board):
	"""
	Allows a user to submit the current version of the currently opened Sudoku board
	:param current_board: The current 9x9 array of the user's submission
	:param blank_board: The original 9x9 array for the user's puzzle, prior to any edits (not utilized by this function)
	"""
	print("You have submitted the current board. Checking if the current board is a valid solution...")
	time.sleep(1)
	copied_board = list(current_board)
	submission_result = main_sudoku.validate_user_submission(user_board=copied_board)

	for line in submission_result:
		time.sleep(0.5)
		print(line)


def user_solve(puzzle_for_user_to_solve):

	time.sleep(1)

	user_board = list(puzzle_for_user_to_solve)

	main_sudoku.npdisplay(user_board)

	valid_selections = {}	

	# Allow the user to set the number in a cell
	option_1 = 'Place a number in an empty cell of this Sudoku board.'
	valid_selections[1] = user_place

	# Allow the user to submit a solution
	option_2 = 'Submit the Sudoku board and see if you have solved this puzzle.'
	valid_selections[2] = user_submit

	# Allow the user to reset the board
	option_3 = 'Reset this Sudoku board. Warning: All progress will be lost!'
	valid_selections[3] = None

	# Allow the user to quit, returning them to puzzle selection
	option_4 = 'Close this Sudoku board, and return to the Puzzle Selection Menu for this puzzle.'
	valid_selections[4] = None

	running = True

	while running:

		print(f"""
		You are currently solving this puzzle.
		Please enter one of the following options:

		1. {option_1}
		2. {option_2}
		3. {option_3}
		4. {option_4}

		Or enter 'Q' to quit Console Sudoku.
		""")

		user_selection = input('Enter your selection: ')

		if user_selection == 'Q':
			return False

		else:
			validated_input = get_valid_int(provided_input=user_selection)

			if validated_input is None:
				print("Error, invalid input. Please enter a number selecting one of the provided options or enter 'Q' to quit Console Sudoku.")

			elif validated_input not in valid_selections:
				print("Error, invalid selection. Please enter one of the provided options or enter 'Q' to quit Console Sudoku.")

			elif validated_input == 3:
				print("You have reset this Sudoku board.")
				time.sleep(1)
				user_board = list(puzzle_for_user_to_solve)
				main_sudoku.npdisplay(user_board)

			elif validated_input == 4:
				print("Returning to the Puzzle Selection Menu for this puzzle.")
				time.sleep(1)
				return True
			else:
				valid_selections[validated_input](current_board=user_board, blank_board=puzzle_for_user_to_solve)


	

def load_sudoku_board(board_to_load):

	time.sleep(1)

	copy_of_board_to_load = list(board_to_load)

	main_sudoku.npdisplay(copy_of_board_to_load)

	valid_selections = {}

	# Allow user to attempt to solve the puzzle
	option_1 = 'Attempt to solve this puzzle.'
	valid_selections[1] = user_solve

	# Allow user to confirm the puzzle is valid
	option_2 = 'Confirm this is a valid sudoku puzzle (confirm there is at least one possible solution).'
	valid_selections[2] = confirm_solvable

	# Allow user to view a solution
	option_3 = 'Generate a valid solution to this puzzle.'
	valid_selections[3] = generate_solution

	# Allow user to return to puzzle selection
	option_4 = 'Return to the Main Menu.'
	valid_selections[4] = None


	running = True

	while running:

		print(f"""
		This is the Puzzle Selection Menu.
		Please enter one of the following options:

		1. {option_1}
		2. {option_2}
		3. {option_3}
		4. {option_4}

		Or enter 'Q' to quit Console Sudoku.
		""")

		user_selection = input('Enter your selection: ')

		if user_selection == 'Q':
			return False

		else:
			validated_input = get_valid_int(provided_input=user_selection)

			if validated_input is None:
				print("Error, invalid input. Please enter a number selecting one of the provided options or enter 'Q' to quit Console Sudoku.")

			elif validated_input not in valid_selections:
				print("Error, invalid selection. Please enter one of the provided options or enter 'Q' to quit Console Sudoku.")

			elif validated_input == 4:
				print("Returning to the Main Menu of Console Sudoku.")
				time.sleep(1)
				return True
			else:
				valid_selections[validated_input](copy_of_board_to_load)



def load_random_sudoku():
	selection = random.choice(puzzles)

	selection_prompt = [
	f"You have selected a Sudoku puzzle called '{selection['puzzle_name']}'.",
	f"This source of this puzzle is {selection['source']}."
	]

	for line in selection_prompt:
		time.sleep(0.5)
		print(line)


	copy_of_selection = list(selection['puzzle'])


	return load_sudoku_board(board_to_load=copy_of_selection)



# Modified from source: https://pynative.com/python-check-user-input-is-number-or-string
def get_valid_int(provided_input):
    try:
        # Convert it into integer
        val = int(provided_input)
        return val
    except ValueError:
        try:
            # Convert it into float
            val = float(provided_input)
            return val
        except ValueError:
            return None


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




	running = True

	while running:

		print(f"""
		This is the Console Sudoku Main Menu.
		Please enter one of the following options:
		
		1. {option_1}
		2. {option_2}

		Or enter 'Q' to quit Console Sudoku.
		""")

		user_selection = input('Enter your selection: ')

		if user_selection == 'Q':
			running = False

		else:
			validated_input = get_valid_int(provided_input=user_selection)

			if validated_input is None:
				print("Error, invalid input. Please enter a number selecting one of the provided options or enter 'Q' to quit Console Sudoku.")

			elif validated_input not in valid_selections:
				print("Error, invalid selection. Please enter one of the provided options or enter 'Q' to quit Console Sudoku.")

			else:
				running = valid_selections[validated_input]()

	print('Thank you for using Console Sudoku.')



# when run as a script, run the console sudoku interface
if __name__ == '__main__':

	welcome()

	present_options()


