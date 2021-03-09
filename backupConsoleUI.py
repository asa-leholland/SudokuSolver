# filename: consoleSudokuUI.py
# author: Asa Holland

import random
import time

import re

import main as main_sudoku


import json


def welcome():
	"""
	Welcomes the user to Console Sudoku.
	"""
	print("""
		Welcome to Console Sudoku!""")


def describe_sudoku():
	print('The goal of Sudoku is to completely fill a 9×9 grid with digits. When filled with valid digits, every column, every row, and every 3×3 subgrid that compose the game board contain each digit from 1 to 9. The Sudoku player is provided a grid which is partially complete (some cells are left blank), and the Sudoku player aims to fill in the grid with valid digits so that the puzzle can be completed. If enough blanks are present when the board is first presented, it is possible for multiple valid solutions to exist for a single board, but a good instance of a Sudoku puzzle has only one single valid solution.')

	time.sleep(3)

	return True


def generate_solution(board):
	print('\nChecking for a solution...')
	time.sleep(2)
	board_copy = list(board)
	if main_sudoku.solve_sudoku(board_to_solve=board_copy):

		print('\nOne valid solution to this Sudoku puzzle is as follows:\n')
		main_sudoku.npdisplay(board_copy)
	else:
		print('\nThere is no valid solution for this puzzle.')
	time.sleep(1)
	


def user_solve(puzzle_for_user_to_solve, backup):

	time.sleep(1)

	user_board = list(puzzle_for_user_to_solve)

	main_sudoku.npdisplay(user_board)

	running = True

	while running:

		print(f"""
		You are currently solving this puzzle.
		Please enter one of the following options:

		1. Place a number in an empty cell of this Sudoku board.
		2. Submit this Sudoku board and verify if this puzzle has been solved.
		3. Reset this Sudoku board. Warning: All progress will be lost!
		4. Close this Sudoku board, and return to the Puzzle Selection Menu for this puzzle.

		Or enter 'Q' to quit Console Sudoku.
		""")

		user_selection = input('Enter your selection: ')

		if user_selection == 'Q':
			return False

		else:
			validated_input = get_valid_int(provided_input=user_selection)

			if validated_input is None:
				print("Error, invalid input. Please enter a number selecting one of the provided options or enter 'Q' to quit Console Sudoku.")

			elif validated_input not in {1, 2, 3, 4}:
				print("Error, invalid selection. Please enter one of the provided options or enter 'Q' to quit Console Sudoku.")

			# Allow the user to set the number in a cell
			elif validated_input == 1:
				user_input = input("Please enter the Row, Column, Value you would like to place: ")
				time.sleep(1)

				# Check if the user input is valid
				is_valid_input = bool(re.match(r"^[0-8], [0-8], [1-9]$", user_input))
				if not is_valid_input:
					print("""Invalid entry. To enter 2 in Row 3, Column 4, enter '2, 3, 4'.""")

				else:

					# Parse the user provided input
					[user_row, user_column, user_value] = [int(digit) for digit in user_input.split(', ')]

					# Check if the user input would change an original cell
					if user_board[user_row][user_column] != 0:
						print("""Invalid placement. You can't change cells from the original provided puzzle.""")

					else:
						user_board[user_row][user_column] = user_value
						print(f"""Valid placement. You have placed a {user_value} in Row {user_row}, Column {user_column}.""")
				
				main_sudoku.npdisplay(user_board)
			
			# Allow the user to submit a solution
			elif validated_input == 2:
				print("You have submitted the current board. Checking if the current board is a valid solution...")
				time.sleep(1)
				copied_board = list(user_board)
				submission_result = main_sudoku.validate_user_submission(user_board=copied_board)

				for line in submission_result:
					time.sleep(0.5)
					print(line)

				main_sudoku.npdisplay(user_board)

			# Allow the user to reset the board
			elif validated_input == 3:
				print("You have reset this Sudoku board.")
				time.sleep(1)
				user_board = list(backup)
				main_sudoku.npdisplay(user_board)

			# Allow the user to quit, returning them to puzzle selection
			elif validated_input == 4:
				print("Returning to the Puzzle Selection Menu for this puzzle.")
				time.sleep(1)
				return True


	

def load_sudoku_board(board_to_load):

	time.sleep(1)

	copy_of_board_to_load = list(board_to_load)
	second_copy = list(board_to_load)

	main_sudoku.npdisplay(copy_of_board_to_load)

	valid_selections = {}

	
	option_1 = '.'
	valid_selections[1] = user_solve

	# # Allow user to confirm the puzzle is valid
	# option_2 = 'Confirm this is a valid sudoku puzzle (confirm there is at least one possible solution).'
	# valid_selections[2] = confirm_solvable

	
	option_2 = ''
	valid_selections[2] = generate_solution

	
	option_3 = ''
	valid_selections[3] = None


	running = True

	while running:

		print(f"""
		This is the Puzzle Selection Menu.
		Please enter one of the following options:

		1. Attempt to solve this puzzle.
		2. Generate and view a valid solution to this puzzle.
		3. Return to the Main Menu.

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

			# Allow user to attempt to solve the puzzle
			elif validated_input == 1:
				user_solve(puzzle_for_user_to_solve=copy_of_board_to_load, backup=second_copy)
			
			# Allow user to view a solution
			elif validated_input == 2:
				duplicate = list(board_to_load)
				generate_solution(board=duplicate)

			# Allow user to return to puzzle selection
			elif validated_input == 3:
				print("Returning to the Main Menu of Console Sudoku.")
				time.sleep(1)
				return True
			else:
				running = valid_selections[validated_input](copy_of_board_to_load)



def load_random_sudoku():

	with open(f"puzzles.json") as json_file:
		data = json.load(json_file)
		random_puzzle = random.choice(data)

	name = random_puzzle["puzzle_name"]
	source = random_puzzle["source"]

	selection_prompt = [
	f"You have selected a Sudoku puzzle called '{name}'.",
	f"This source of this puzzle is {source}."
	]

	for line in selection_prompt:
		time.sleep(0.5)
		print(line)


	copy_of_selection = list(random_puzzle["puzzle"])


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


