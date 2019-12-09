print("DATA ANALYSIS 1")
#Beyond the Coding: Files verses Data structures (lists)

#	Files are used to store the data so the data remains when
#	the program isn't running.  A data structure is where the data
#	lives when the program is running.  When using data from files
#	it must be copied into a file.  When the program is done running
#	the information must be copied back into the file.

#Beyond the Coding:  
#	Knowing how the data in your file is organizedis essential.  The 
#	algoritms used to format the data into something that is useable 
#	is based on knowing how it is stored. 

#Big Skill: Reading from text file.
data = open("dataAnalysis1.txt","r"); 
dataString = data.read()
dataList = dataString.split("\n")

#Beyond the Coding:  
#	The order of the data could be important
#	if any of the analysis requires changing 
#	the order you need to make a copy of the 
#	information
#
print(dataList)

#Big Skill: Looping through a list using counted loop.  
for i in range(0, len(dataList),1):
	#Big Skill: Removing Elements
	dataList[i] = dataList[i].replace(",","")
	#Big Skill: Casting
	dataList[i] = float(dataList[i])

print(dataList)