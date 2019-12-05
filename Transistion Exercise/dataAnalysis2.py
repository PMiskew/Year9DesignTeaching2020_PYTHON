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
#Find smallest
#Find mean, median, mode
#Remove outliers (inner quartile range)
