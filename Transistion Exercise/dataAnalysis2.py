print("DATA ANALYSIS 2")
data = open("randomDataRAW.txt"); 
dataString = data.read()
dataList = dataString.split("\n")

print(dataList)

#Big Skill: Looping through a list using counted loop.  
for i in range(0, len(dataList),1):
	#Big Skill: Removing Elements
	dataList[i] = dataList[i].replace(",","")
	#Big Skill: Casting
	dataList[i] = float(dataList[i])

print(dataList)


#Big Skill: When finding max or min element in list alaways
#			set the max/min to an element in the list

#Find largest
max = dataList[0] #always set to an exisiting element

for i in range(0, len(dataList),1):
	if dataList[i] > max:
		max = dataList[i]

print(max)


#Find smallest
min = dataList[0] #always set to an existing element
for i in range(0, len(dataList),1):
	if dataList[i] < min:
		min = dataList[i]

print(max)

#Sort a datalist
dataListsorted = dataList.sort()

#Find mean, median, mode
streak = 0;
streakStartIndex = 0;

for i in range(0, len())


#Remove outliers (inner quartile range)
