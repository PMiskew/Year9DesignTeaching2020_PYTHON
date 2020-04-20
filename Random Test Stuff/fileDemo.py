
user = input("Are your new user? ")
userName = ""
if user == "yes":
	userName = input("What is your name: ")
else:
	userName = input("What is your username: ")

f = open(userName+".txt","a")


f.close()