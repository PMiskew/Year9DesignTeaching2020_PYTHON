'''
This program is a reproduction of
https://medium.com/analytics-vidhya/understanding-genetic-algorithms-in-the-artificial-intelligence-spectrum-7021b7cc25e7
'''
import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
population = []
fit = []
ps = 10 #population size

word = ["b","a","n","a","n","a"] 
wsize = len(word)

def generatePopulation(populationSize, wordSize):
	
	for i in range(0,populationSize,1):
		
		gword = ""
		
		for j in range(0,wordSize,1):

			gword = gword + letters[random.randint(0,len(letters)-1)]

		population.append(gword)

def defineFit(word, wordSize):

	for i in range(0, len(population),1):
		
		fitvalue = 0

		for j in range(0,wordSize,1):

			if population[i][j] in word:

				fitvalue = fitvalue + 1

		fit.append(fitvalue)

def repopulate(populationSize):

	seedPopulation = []

	#generate seed population
	for i in range(0,len(fit),1):
		if fit[i] > 0:
			seedPopulation.append(population[i])

	population.clear()
	fit.clear()
	for i in range(0, populationSize,1):
		parent1 = seedPopulation[random.randint(0,len(seedPopulation)-1)]
		parent2 = seedPopulation[random.randint(0,len(seedPopulation)-1)]
		population.append(parent1[0:3] + parent2[3:])




generatePopulation(ps,wsize)
print(population)


for i in range(0,100,1):
	defineFit(word,wsize)
	print(fit)
	repopulate(ps)
	print(population)
	print("\n\n")
