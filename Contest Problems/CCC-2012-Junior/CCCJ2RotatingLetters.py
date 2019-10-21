
'''
Student Questions

Should I copy the string into an array?
	No, this is an extra step and even thought it will work
	it will mean the program is slower as the length increases

'''

'''
Approach A is a standard approach most students
use
'''
def rotatingLettersA():

	str = "SHINS"

	for i in range(0,len(str),1):

		if str[i] != "I" and str[i] != "O" and str[i] != "S" and str[i] != "H" and str[i] != "Z" and str[i] != "X" and str[i] != "N":
			return "NO"

	
	return "YES"

def rotatingLettersB():

	str = "SHINS"
	
	str = str.replace("I","")
	str = str.replace("O","")
	str = str.replace("S","")
	str = str.replace("H","")
	str = str.replace("Z","")
	str = str.replace("X","")
	str = str.replace("N","")
	
	if len(str) == 0:
		return "YES"
	return "NO"
	

#MAIN CODE
print(rotatingLettersB())

