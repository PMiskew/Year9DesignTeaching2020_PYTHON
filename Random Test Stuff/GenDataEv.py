import random

list = []
goal = 50
setsize = 10
fitTolerance = 10 #percentage 
populationGenSize = 10 #Number of samples used for next generation

#INITAL POPULATION
for i in range(0,setsize,1):
	list.append(random.randint(0,100))


while (True):

	#ASSESS FITNESS
	#Defined as offset from goal
	fit = []
	populationSeed = []

	for i in range(0,setsize,1):
		fit.append(abs(list[i] - goal))

	#PICK MOST FIT
	for i in range (0,setsize,1):
		if fit[i] < fittolerance:
			populationSeed.append(list[i])


	#GENERATE NEXT GENERATION

	print(list)
	print(fit)

