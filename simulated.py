import math
import random

from tspFunctions import getNeighbors
from  tspFunctions import  travelValue
from tspFunctions import graph
from tspFunctions import graph2
from math import e
from datetime import datetime


def simulatedAnnealing(s,graph,iterations,maxTemp,minTemo):
    current = s
    temp = maxTemp
    for i in range(iterations):
        temp = schedule(maxTemp,temp,0.5)
        if temp == 0:
            return current
        neighbor = randomSuccesor(current)
        deltaE = travelValue(graph,current) - travelValue(graph,neighbor)
        if deltaE > 0:
            current = neighbor
        else:
            if probality(deltaE,temp):
                current = neighbor
    return current

def schedule(maxTemp,temp,cr):
    return temp* cr

def randomSuccesor(state):
    neighbors = getNeighbors(state)
    randomN = random.randint(0,len(neighbors)-1)
    return neighbors[randomN]

def probality(deltaE,t):
    prob = math.pow(e,deltaE/t)
    return random.random() < prob

s = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
start_time = datetime.now()
best = simulatedAnnealing(s,graph2,1000,2500,0)
value = travelValue(graph2,best)
end_time = datetime.now()
print("the best solution is:")
print(best)
print("the value of the result is: ",value)
print('Duration: {}'.format(end_time - start_time))


