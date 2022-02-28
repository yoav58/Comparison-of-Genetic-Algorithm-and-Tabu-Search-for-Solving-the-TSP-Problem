import numpy as np
import random
from datetime import datetime

from tspFunctions import travelValue
from tspFunctions import  graph
from tspFunctions import  graph2
# i let the option of two permutation be the same
# because the chance it will happend is very small
def chooseInitialPopulation(startingPopulation,vertexSize):
    population = []
    for i in range(startingPopulation):
        ar = np.random.permutation(vertexSize)
        population.append(ar)
    return population

# calculate the chance of each permotation to be selected
def chanceToSelected(population,graph):
    values = []
    for i in population:
        value = travelValue(graph,i)
        values.append(value)
    # move as chace to selected
    totalValues = sum(values)
    weights = []
    for i in values:
        percentege = 100 - (i/totalValues * 100)
        weights.append(percentege)
    return weights

# return the best population
def choosePopulationWillgrowth(poulation,weights,selected):
    return random.choices(poulation, weights,k=selected)


def crossover(gene1,gene2,vertexSize):
    temp1 = gene1[4:8]
    temp2 = []
    nextI = 0
    for i in range(vertexSize):
        if gene2[i] in temp1:
            continue
        temp2.append(gene2[i])
        if len(temp2) == 4:
            temp2.extend(temp1)
            nextI = i + 1
            break
    for i in range(vertexSize):
        if i < nextI:
            continue
        if gene2[i] in temp1:
            continue
        temp2.append(gene2[i])

    return temp2

def mutation(son):
    while True:
        place1 = random.randint(1,9)
        place2 = random.randint(1,9)
        if place1 != place2:
            temp = son[place1]
            son[place1] = son[place2]
            son[place2] = temp
        return son


def genetic(population,graph,choosen):
    for i in range(1000):
        newPopulation = []
        p = population
        c = choosen
        weights = chanceToSelected(p,graph)
        selected = choosePopulationWillgrowth(p,weights,c)
        for x in range(len(selected)):
            son1 = crossover(selected[x],selected[x+1],19)
            son2 = crossover(selected[x+1],selected[x],19)
            son1 = mutation(son1)
            son2 = mutation(son2)
            newPopulation.append(son1)
            newPopulation.append(son2)
            x += 2;
            if x == len(selected) - 1:
                break
        population = newPopulation
        choosen -= 1
    return bestGene(graph,population)

def bestGene(graph,population):
    best = 0
    for i in range(len(population)):
        if travelValue(graph,population[i]) < travelValue(graph,population[best]):
            best = i
    return population[best]


start_time = datetime.now()
popul = chooseInitialPopulation(10000,19)
percentage = chanceToSelected(popul,graph2)
selected = choosePopulationWillgrowth(popul,percentage,2000)
best = genetic(popul,graph2,2000)
value = travelValue(graph2,best)
end_time = datetime.now()
print("the best solution  is:")
print(best)
print("the travel price is: ",value)
print('Duration: {}'.format(end_time - start_time))

