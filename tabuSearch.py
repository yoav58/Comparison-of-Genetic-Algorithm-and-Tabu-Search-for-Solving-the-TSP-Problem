# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sys import maxsize
from itertools import permutations
import copy
from datetime import datetime
from tspFunctions  import graph2
from tspFunctions import travelValue
from tspFunctions import getNeighbors
def tabuSearchTsp(graph,s,iterations,maxTabu):
    bestTravel = s
    bestCurrent = s
    tabuList = []
    tabuList.append(s)
    for i in range(iterations):
        neighbors = getNeighbors(bestCurrent)
        bestCurrent = neighbors[0]
        for neighbor in neighbors:
            if travelValue(graph,neighbor) < travelValue(graph,bestCurrent) and neighbor not in tabuList:
                bestCurrent = neighbor
        if travelValue(graph,bestCurrent) < travelValue(graph,bestTravel):
            bestTravel = bestCurrent
        tabuList.append(bestCurrent)
        if len(tabuList) > maxTabu:
            tabuList.pop(0)
    return bestTravel

vertex1 = [0,20,6,3,1,4,9,5,10,11,20,1]
vertex2 = [10,0,1,2,3,5,7,8,8,6,4,2]
vertex3 = [3,46,0,6,7,8,9,4,2,3,10,51]
vertex4 = [1,4,3,0,8,6,7,6,5,4,2,1]
vertex5 = [20,4,13,53,0,23,12,11,5,2,5,74]
vertex6 = [32,15,1,23,643,0,2,3,5,6,74,1]
vertex7 = [43,1,43,13,2,23,0,5,65,21,6,15]
vertex8 = [2,10,10,23,3,1,45,0,53,2,14,21]
vertex9 = [7,11,32,11,54,32,24,43,0,23,1,9]
vertex10 = [5,3,18,6,21,15,17,10,15,0,32,7]
vertex11 = [87,4,34,3,1,5,65,43,14,12,0,23]
vertex12 = [12,4,32,67,1,5,2,43,1,8,3,0]

#vertex1 = [0,2,3,4]
#vertex2 = [2,0,7,5]
#vertex3 = [3,7,0,6]
#vertex4 = [4,5,6,0]
s = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#s = [7,5,2,4,11,3,10,9,8,0,1,6]
graph = [vertex1, vertex2, vertex3, vertex4,vertex5,vertex6,vertex7,vertex8,vertex9,vertex10,vertex11,vertex12]
start_time = datetime.now()
result = tabuSearchTsp(graph2,s,1000,500)
value = travelValue(graph2,result)
end_time = datetime.now()
print("the best solution is:")
print(result)
print("the value of the result is: ",value)
print('Duration: {}'.format(end_time - start_time))





