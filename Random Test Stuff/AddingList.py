
#Creates a list
list = [1,4,5,7,6,1,2,3,4,5]

#Write a loop that will print out each index value
#list is a length of 6 there for print out 0 - 5

#Create a variable called sum
sum = 0

for i in range(0, len(list), 1):
	sum = sum + list[i]
	
print(sum)
