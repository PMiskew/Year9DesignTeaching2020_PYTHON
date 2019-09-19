#I don't want to restart the program all the time
#This will loop. 

import os
#Please take an input for name 

name = "Paul"

while name != "exit":

	name = input("What is your name? ")
	#Have the computer say "Hello <name>"
	os.system("say Hello, "+name)