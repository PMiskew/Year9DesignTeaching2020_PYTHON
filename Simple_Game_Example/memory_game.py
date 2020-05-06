import random

'''

This is a text based memory game

'''



board = ["one","one","two","two","three","three","four","four"]
display_board = ["?","?","?","?","?","?","?","?"]
################################################################
#Scramble Board
#
# The below code takes two random elements and swaps them.  
# The method will run this process shuffle_length times. 
#
#################################################################
shuffle_length = 100


for i in range(0, shuffle_length,1):

	r1 = random.randint(0,len(board) - 1)
	r2 = random.randint(0,len(board) - 1)

	temp = board[r1]
	board[r1] = board[r2]
	board[r2] = temp


#check board suffle status
#print(board)

#
#Game loop - Single Player
#
#	This is a loop that runs while there are still elements to match. When a match is made
#	the elements get replaces with X values.  When the entire board is X values it exits.  
#	

while (True):
	
	board_display_line1 = ""
	board_display_line2 = ""

	for i in range(0, len(board), 1):
	
		board_display_line1 = board_display_line1 + "\t"+str(i)
		board_display_line2 = board_display_line2 + "\t"+str(display_board[i])


	print(board_display_line1)
	print(board_display_line2)

	guess1 = input("Flip 1: ")

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


	guess2 = input("Flip 2: ")








