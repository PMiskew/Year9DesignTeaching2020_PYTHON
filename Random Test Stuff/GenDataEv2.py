import random

def printAvg(list):
	total = sum(list)
	avg = total/len(list)
	print(avg)


list = []


goal = 50 #Goal for the populated list
setsize = 10 #Size of desired list
fitTolerance = 10 #Offset from goal 
populationGenSize = 10 #Number of population for next generation
generations = 100 #generations to run
populationSeeds = [] #Stores survising elements
fit = [] #Parallel array designed to store offset of actual from goal 

#INITAL POPULATION
for i in range(0,setsize,1):
	list.append(int(random.randint(0,100)))


print("*********************************************")
print("INITAL POPULATION")
printAvg(list)
print(list)
print("\n\n")
print("*********************************************")


for i in range(0, generations, 1):
	

	populationSeeds.clear() #clear old "survivors"
	fit.clear() # clear old fit values

	#Defined as offset from goal
	for i in range(0,setsize,1):
		fit.append(list[i] - goal)

	#PICK MOST FIT
	for i in range (0,setsize,1):
		if fit[i] < fitTolerance:
			populationSeeds.append(list[i])

	#Populate with random with remaining spots
	for i in range (0,setsize - len(populationSeeds),1):
		populationSeeds.append(list[i])

	#print(fit)
	#print("\t",populationSeeds)
	
	list.clear() #KILL LAST GENERATION - CLEAR LIST
	

	#GENERATE NEXT GENERATION
	for i in range(0,setsize,1):
		parent1 = populationSeeds[random.randint(0,len(populationSeeds) - 1)]
		parent2 = populationSeeds[random.randint(0,len(populationSeeds) - 1)]
		list.append((parent1 + parent2) // 2)
		#MUTATIONS?

	printAvg(list) #Check list avg
	print(list)



