import os
#Please take an input for name 
name = input("What is your name? ")
#Have the computer say "Hello <name>"
os.system("say Hello, "+name)

os.system("say Let me count for you.")
os.system("say What should I count too?")
n = input("")
n = int(n)

for i in range(0,n,1):
	os.system("say "+str(i + 1))