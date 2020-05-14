import random

'''

This is a text based memory game

'''


def shuffle(shuffle_length):

	

	for i in range(0, shuffle_length,1):

		r1 = random.randint(0,len(board) - 1)
		r2 = random.randint(0,len(board) - 1)

		temp = board[r1]
		board[r1] = board[r2]
		board[r2] = temp

board = ["one","one","two","two","three","three","four","four"]
display_board = ["?","?","?","?","?","?","?","?"]
guesses = 0
################################################################
#Scramble Board
#
# The below code takes two random elements and swaps them.  
# The method will run this process shuffle_length times. 
#
#################################################################

shuffle(3) #shuffles the board



#check board suffle status
#print(board)

#
#Game loop - Single Player
#
#	This is a loop that runs while there are still elements to match. When a match is made
#	the elements get replaces with X values.  When the entire board is X values it exits.  
#	

while ("?" in display_board):

	print("")
	print("")
	#####################################################################
	#
	#	DISPLAY BOARD
	#
	#####################################################################	
	board_display_line1 = ""
	board_display_line2 = ""

	#This loop constructs the strings to be displayed 
	for i in range(0, len(board), 1):
	
		board_display_line1 = board_display_line1 + "\t"+str(i)
		board_display_line2 = board_display_line2 + "\t"+str(display_board[i])


	print(board_display_line1)
	print(board_display_line2)



	#####################################################################
	#
	# TAKE INPUT 1
	#
	#####################################################################
	print("")
	print("")
	guess1 = int(input("Flip 1: "))
	print("")
	print("")
	
	#####################################################################
	#
	#	DISPLAY BOARD
	#
	#	WHEN THE BOARD IS DISPLAYED GUESS1 IS SHOWN
	#
	#####################################################################	
	board_display_line1 = ""
	board_display_line2 = ""

	for i in range(0, len(board), 1):
	
		board_display_line1 = board_display_line1 + "\t"+str(i)
		
		if i == guess1:
			board_display_line2 = board_display_line2 + "\t"+str(board[i])
		else:
			board_display_line2 = board_display_line2 + "\t"+str(display_board[i])

	print(board_display_line1)
	print(board_display_line2)

	#####################################################################
	#
	# TAKE INPUT 2
	#
	#####################################################################
	print("")
	print("")
	guess2 = int(input("Flip 2: "))
	print("")
	print("")
	
	#####################################################################
	#
	#	DISPLAY BOARD
	#
	#	WHEN THE BOARD IS DISPLAYED GUESS1 AND GUESS 2 IS SHOWN
	#
	#####################################################################
	board_display_line1 = ""
	board_display_line2 = ""

	for i in range(0, len(board), 1):
	
		board_display_line1 = board_display_line1 + "\t"+str(i)
		
		if i == guess1 or i == guess2:
			board_display_line2 = board_display_line2 + "\t"+str(board[i])
		else:
			board_display_line2 = board_display_line2 + "\t"+str(display_board[i])
	
	print(board_display_line1)
	print(board_display_line2)
	print("")
	print("")
	if (board[guess1] == board[guess2]):
		print("***************************MATCH***************************")
		display_board[guess1] = ' '
		display_board[guess2] = ' '
	else:
		print("************************NO MATCH***************************")
	print("")
	print("")
	guesses = guesses + 1
	input("Press Enter to continue...")

print("")
print("")
print("THANKS FOR PLAYING!")
print("It took you",guesses,"to get all the matches")
print("")
print("")
