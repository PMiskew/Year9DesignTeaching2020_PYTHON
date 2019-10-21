#This is a reproduction of the example from the below site
'''
https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3
'''
import random

population = []
desire = "010101"


def generatePopulation(size,genes):

	for i in range(0,size,1):
		chromosome = ""
		for j in range(0,genes,1):

			chromosome = chromosome + str(random.randint(0,1))

		population.append(chromosome)


#Main Code
generatePopulation(10,6)
print(population)






