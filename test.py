# test.py



# import numpy to handle array board
import numpy as np 

# source: https://www.geeksforgeeks.org/print-colors-python-terminal/
def prRed(text): print("\033[91m {}\033[00m" .format(text)) 
def prGreen(text): print("\033[92m {}\033[00m" .format(text)) 
def prYellow(text): print("\033[93m {}\033[00m" .format(text)) 
def prLightPurple(text): print("\033[94m {}\033[00m" .format(text)) 
def prPurple(text): print("\033[95m {}\033[00m" .format(text)) 
def prPurpleStarter(text): print("\033[95m {}\033[00m" .format(text), end='') 
def prCyan(text): print("\033[96m {}\033[00m" .format(text)) 
def prLightGray(text): print("\033[97m {}\033[00m" .format(text)) 
def prBlack(text): print("\033[98m {}\033[00m" .format(text)) 

def npdisplay(board):
	"""
	Function to convert the provided puzzle to a numpy array, which is output as a square board
	"""

	#   0 1 2 3 4 5 6 7 8	(purple)
	# 0 1 2 3 4 5 6 7 8 9 	(purple first char, then white background with black text)

	column_header = '  0 1 2 3 4 5 6 7 8'
	prPurple(column_header)

	for index, row in enumerate(board):
		print(str(index), end='')
		row_chars = ''
		for digit in row:
			if digit == 0:
				print()
			else:
				row_chars += str(digit) + ' '

			print(' ')
		print('\n')

	print(np.array(board)) 




fill_in_puzzle = [
		[0,0,0, 0,0,0, 0,0,0],
		[0,0,0, 0,0,0, 0,0,0],
		[0,0,0, 0,0,0, 0,0,0],

		[0,0,0, 1,2,3, 0,0,0],
		[0,0,0, 4,0,6, 0,0,0],
		[0,0,0, 7,8,9, 0,0,0],

		[0,0,0, 0,0,0, 0,0,0],
		[0,0,0, 0,0,0, 0,0,0],
		[0,0,0, 0,0,0, 0,0,0]
		]

npdisplay(fill_in_puzzle)