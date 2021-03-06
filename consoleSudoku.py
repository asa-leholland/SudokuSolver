# filename: consoleSudokuUI.py
# author: Asa Holland

# Import random to randomly select which puzzle is chosen
import random

# import regex to match validity for user-provided input
import re

# import json to read and handle the Sudoku puzzle library (which is stored in a .json format) 
import json

# perform a local import to load the main sudoku verification and solving functions
import main as main_sudoku


def welcome():
	"""
	Welcomes the user to Console Sudoku.
	"""
	print("""
		Welcome to Console Sudoku!""")


def describe_sudoku():
	"""
	Outputs the general rules of Sudoku when the User selects the relevant option on the Console Sudoku Main Menu.
	"""
	print('The goal of Sudoku is to completely fill a 9×9 grid with digits. When filled with valid digits, every column, every row, and every 3×3 subgrid that compose the game board contain each digit from 1 to 9. The Sudoku player is provided a grid which is partially complete (some cells are left blank), and the Sudoku player aims to fill in the grid with valid digits so that the puzzle can be completed. If enough blanks are present when the board is first presented, it is possible for multiple valid solutions to exist for a single board, but a good instance of a Sudoku puzzle has only one single valid solution.')
	return True


def generate_solution(board):
	"""
	Provided a Sudoku board, check to see if there is a possible solution for that board, and if there is, generate and display it for the user.
	"""

	# Notify the user what is being done
	print('\nChecking for a solution...')

	# convert the provided board into a duplicate so no changes are made to the original board
	board_copy = list(board)

	# Check if the board is solvable
	if main_sudoku.solve_sudoku(board_to_solve=board_copy):

		# If the board is solvable, let the user know that is is solvable and disply the valid solution generated by the solving algorithm
		print('\nOne valid solution to this Sudoku puzzle is as follows:\n')
		main_sudoku.npdisplay(board_copy)

	# If the board is not solvable, let the user know.
	else:
		print('\nThere is no valid solution for this puzzle.')
	


def user_solve(puzzle_for_user_to_solve, backup):
	"""
	Provided two copies of a sudoku board, allow the user to make changes to one.
	"""

	# duplicate the provided user board to ensure no changes are made to the original
	user_board = list(puzzle_for_user_to_solve)

	# display the current user Sudoku board 
	main_sudoku.npdisplay(user_board)

	# start a flag indicating the user is currently accessing the puzzle
	running = True
	while running:

		# Before each step taken by the user, display the in-game menu options
		print(f"""
		You are currently solving this puzzle.
		Please enter one of the following options:

		1. Place a number in an empty cell of this Sudoku board.
		2. Submit this Sudoku board and verify if this puzzle has been solved.
		3. Reset this Sudoku board. Warning: All progress will be lost!
		4. Close this Sudoku board, and return to the Puzzle Selection Menu for this puzzle.

		Or enter 'Q' to quit Console Sudoku.
		""")

		# prompt the user for their input
		user_selection = input('Enter your selection: ')

		# handle user requst to quit the game
		if user_selection == 'Q':
			return False

		# in all other cases...
		else:

			# First, validate the user input
			validated_input = get_valid_int(provided_input=user_selection)

			# If the user's input was invalid, prompt the user and return to the running loop 
			if validated_input is None:
				print("Error, invalid input. Please enter a number selecting one of the provided options or enter 'Q' to quit Console Sudoku.")

			# If the user's input was a valid integer but not a valid option, prompt the user with the mistake.
			elif validated_input not in {1, 2, 3, 4}:
				print("Error, invalid selection. Please enter one of the provided options or enter 'Q' to quit Console Sudoku.")

			# Allow the user to set the number in a cell
			elif validated_input == 1:

				# prompt user with instruction
				user_input = input("Please enter the Row, Column, Value you would like to place: ")

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

					# If the user input will not change the default puzzle values, place the value and output the change made to the user's board
					else:
						user_board[user_row][user_column] = user_value
						print(f"""Valid placement. You have placed a {user_value} in Row {user_row}, Column {user_column}.""")
				
				# Regardless of whethter the input was valid or invalid, display the updated board
				main_sudoku.npdisplay(user_board)
			
			# Allow the user to submit a solution
			elif validated_input == 2:

				# prompt the user that the validation is occuring
				print("You have submitted the current board. Checking if the current board is a valid solution...")

				# duplicate the board and run the validation algoroithm on the duplicate to confirm whether it is valid or not 
				copied_board = list(user_board)
				submission_result = main_sudoku.validate_user_submission(user_board=copied_board)

				# Output each line of the result of the validation check
				for line in submission_result:
					print(line)

				# Output the board
				main_sudoku.npdisplay(user_board)

			# Allow the user to reset the board
			elif validated_input == 3:
				print("You have reset this Sudoku board.")
				user_board = list(backup)
				main_sudoku.npdisplay(user_board)

			# Allow the user to quit, returning them to puzzle selection
			elif validated_input == 4:
				print("Returning to the Puzzle Selection Menu for this puzzle.")
				return True


	

def load_sudoku_board(board_to_load):
	"""
	Loads a selected sudoku board into the Puzzle Selection Menu, allowing the user to solve the puzzle or generate a solution.
	"""

	# duplicate the board so changes are kept locally
	copy_of_board_to_load = list(board_to_load)
	second_copy = list(board_to_load)

	# display the loaded board
	main_sudoku.npdisplay(copy_of_board_to_load)

	# start tracking running
	running = True
	while running:

		# Output the Puzzle Selection options
		print(f"""
		This is the Puzzle Selection Menu.
		Please enter one of the following options:

		1. Attempt to solve this puzzle.
		2. Generate and view a valid solution to this puzzle.
		3. Return to the Main Menu.

		Or enter 'Q' to quit Console Sudoku.
		""")

		# obtain the user input
		user_selection = input('Enter your selection: ')

		# allow the user to quit Console Sudoku
		if user_selection == 'Q':
			return False

		# In all other cases
		else:

			# confirm that the user provided valid input
			validated_input = get_valid_int(provided_input=user_selection)

			# if the user did not provided valid input, let them know
			if validated_input is None:
				print("Error, invalid input. Please enter a number selecting one of the provided options or enter 'Q' to quit Console Sudoku.")

			# If the user provided valid input but not a valid selection, let them know
			elif validated_input not in {1, 2, 3}:
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

				return True
			else:
				running = valid_selections[validated_input](copy_of_board_to_load)


def load_random_sudoku():
	"""
	Loads a random sudoku puzzle from the puzzle libary (json file)
	"""

	# open the json file that stores the Sudoku puzzles
	with open(f"puzzles.json") as json_file:
		data = json.load(json_file)

		# select a random puzzle
		random_puzzle = random.choice(data)

	# Identify the puzzle name and source
	name = random_puzzle["puzzle_name"]
	source = random_puzzle["source"]

	# notify the user that a puzzle has been selected and output the name and source of the Sudoku puzzle
	selection_prompt = [
	f"You have selected a Sudoku puzzle called '{name}'.",
	f"This source of this puzzle is {source}."
	]
	for line in selection_prompt:
		print(line)

	# create a local copy of the puzzle that the user can load
	copy_of_selection = list(random_puzzle["puzzle"])

	# return the loaded sudoku board
	return load_sudoku_board(board_to_load=copy_of_selection)


# Modified from source: https://pynative.com/python-check-user-input-is-number-or-string
def get_valid_int(provided_input):
	"""
	Short function to validate the provided user input
	"""

	# Attempt to convert the provided input to an integer and return that integer
	try:
		val = int(provided_input)
		return val

	# If a value error occurs, the input is either a float or a string
	except ValueError:

		# attempt to convert the input to a float and return that
		try:
			val = float(provided_input)
			return val
		
		# if that doesn't work, return None (the input is not valid)
		except ValueError:
			return None


def present_options():
	"""
	Present user with options to select from on the Console Sudoku Main Menu
	"""

	# create a dictionary to store the options
	valid_selections = {}

	# Allow user to read a description about Sudoku
	option_1 = 'Read a short description about the rules of Sudoku.'
	valid_selections[1] = describe_sudoku

	# Allow user to open a random sudoku puzzle from library
	option_2 = 'Load a random Sudoku puzzle from the Puzzle Library.'
	valid_selections[2] = load_random_sudoku

	# start running the Comsole Sudoku Main Menu
	running = True
	while running:

		# Present the user with their options
		print(f"""
		This is the Console Sudoku Main Menu.
		Please enter one of the following options:
		
		1. {option_1}
		2. {option_2}

		Or enter 'Q' to quit Console Sudoku.
		""")

		# allow the user to provide input
		user_selection = input('Enter your selection: ')

		# Allow the user to exit console sudoku
		if user_selection == 'Q':
			running = False

		# in all other cases
		else:

			# validate the user input
			validated_input = get_valid_int(provided_input=user_selection)

			# if the user input is not valid, prompt the user accordingly
			if validated_input is None:
				print("Error, invalid input. Please enter a number selecting one of the provided options or enter 'Q' to quit Console Sudoku.")

			# if the input is valid but not a legal option, let the user know.
			elif validated_input not in valid_selections:
				print("Error, invalid selection. Please enter one of the provided options or enter 'Q' to quit Console Sudoku.")

			# otherwise, run the selected option
			else:
				running = valid_selections[validated_input]()

	print('Thank you for using Console Sudoku.')



# when run as a script, run the console sudoku interface
if __name__ == '__main__':

	welcome()
	present_options()


