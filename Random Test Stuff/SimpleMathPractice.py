import os
import random
#This is a program for a young child
#that wants to practice simple addition

name = input("What is your name: ")
os.system("say hi," + name)

a = random.randint(0,10)
b = random.randint(0,10)

os.system("say What is "+str(a)+"+"+str(b)+"?")
print("What is "+str(a)+"+"+str(b)+"?")

