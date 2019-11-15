
#How do I print out 1 to 5
print("1")
print("2")
print("3")
print("4")
print("5")
print("***********")
#Problem is what about 1 to 500 or 1 to 5000000 or -345 to 367

#Observation: There is a pattern!
# A loop structure, sepcifically a for loop can be used to represent patters. 

for i in range(1, 5, 1):
	print(i)

#TRACE 
#
#	When we first get to the loop i = 1
#	
#		i |	i < 5 - ?			| 
#		1 | 1 < 5 - VRAI (T)	| RUN THE LOOP
#		2 | 2 < 5 - VRAI (T)	| RUN THE LOOP
#		3 | 3 < 5 - VRAI (T)	| RUN THE LOOP
#		4 | 4 < 5 - VRAI (T) 	| RUN THE LOOP
#		5 | 5 < 5 - FAUX (F)	| EXIT THE LOOP
#
# HOW MANY TIMES DID THIS LOOP RUN? 4 TIMES
# SHORT CUT FOR CALCUATING THE NUMBER OF TIMES - 5 - 1 = 4



#<count>,<check>,<change>
#check is always count < check
#the variable i is your counting variable.  It can be anything
for i in range(1, 501, 1):
	print(i)


print("**************")
for i in range(-345,368,1):
	#LOOP CODE BLOCK
	print(i)


print("**************")
print("Print out even numbers from 2 to 456 (inclusive)")
for i in range(2,457,2):
	print(i)

print("**************")
print("I HAVE PROBLEM I WANT TO COUNT FROM 345 down to -45")
for i in range(345,-46,-1):
	print(i)

#Why don't we use 
word = "Paul"

for letters in word:
	print (letters)


