
#creates a variable data that points at the file and 
#is prepared to read from it. 
data = open("randomDataRAW.txt","r") #Opens the file


dataString = data.read() #reads all the content from the file and stores it as a stirng
#print(dataString)

#copy the data from the string into a list
dataList = dataString.split("\n") #takes the string and converts it to a list of strings using \n as inicator for new element

#print(dataList)

#Cast all the list elements into floats
#   0    1     2 
# ["1","3.32","5.43"]
for i in range(0, len(dataList),1): #loops through every element
	dataList[i] = dataList[i].replace(",","") #replace all the , with ""
	dataList[i] = float(dataList[i]) #cast the element to a float


print(dataList)