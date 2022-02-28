import copy

def travelValue(graph,s):
    value = 0
    sizeOfTravel = len(s)
    for i in range(sizeOfTravel):
        if i == (sizeOfTravel - 1):
            city1 = s[i]
            city2 = s[0]
            value += graph[city1][city2]
            continue
        city1 = s[i]
        city2 = s[i+1]
        value += graph[city1][city2]
    return value


def getNeighbors(s):
    neighbors = []
    numberOfcities = len(s)
    for i in range(numberOfcities):
        if i == numberOfcities:
            return neighbors
        r = i+1
        for x in range(i+1,numberOfcities):
            copyState = copy.deepcopy(s)
            copyState[i],copyState[x] = s[x],s[i]
            x += 1
            neighbors.append(copyState)
    return neighbors


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
graph = [vertex1, vertex2, vertex3, vertex4,vertex5,vertex6,vertex7,vertex8,vertex9,vertex10,vertex11,vertex12]

vertex11 = [0,20,6,3,1,4,9,5,10,11,20,1,50,32,5,7,10,85,31,1]
vertex22 = [10,0,1,2,3,5,7,8,8,6,4,2,1,45,7,43,15,2,8,90]
vertex33 = [3,46,0,6,7,8,9,4,2,3,10,51,54,8,1,32,13,23,21,11]
vertex44 = [1,4,3,0,8,6,7,6,5,4,2,1,5,3,7,21,67,31,45,12,4]
vertex55 = [20,4,13,53,0,23,12,11,5,2,5,74,13,14,15,16,17,18,19,20]
vertex66 = [32,15,1,23,643,0,2,3,5,6,74,1,64,27,42,88,12,11,1,20]
vertex77 = [43,1,43,13,2,23,0,5,65,21,6,15,64,23,86,33,6,4,8,90]
vertex88 = [2,10,10,23,3,1,45,0,53,2,14,21,11,87,4,56,74,32,11,3]
vertex99 = [7,11,32,11,54,32,24,43,0,23,1,9,13,75,34,11,14,4,7,1]
vertex1010 = [5,3,18,6,21,15,17,10,15,0,32,7,15,75,24,99,3,23,43,10]
vertex1111 = [87,4,34,3,1,5,65,43,14,12,0,23,76,1,3,2,6,3,2,4,6,4,3]
vertex1212 = [12,4,32,67,1,5,2,43,1,8,3,0,12,3,4,6,1,1,1,1]
vertex13 = [12,4,32,67,1,5,2,43,4,8,3,21,0,32,1,53,2,7,12,20]
vertex14 = [8,14,32,67,1,5,2,43,4,8,3,21,10,0,1,53,2,5,12,20]
vertex15 = [8,14,32,67,3,55,12,4,2,4,3,21,10,20,0,53,2,25,1,20]
vertex16 = [8,14,32,7,3,55,12,5,11,4,3,212,10,20,23,0,2,25,1,42]
vertex17 = [2,14,32,7,34,55,12,5,11,61,3,22,10,20,23,4,0,2,1,42]
vertex18 = [2,14,32,6,54,55,12,4,11,61,3,2,3,90,23,4,11,0,12,31]
vertex19 = [2,14,32,6,54,55,12,4,11,61,3,2,3,90,23,4,11,2,0,321]
vertex20 = [15,8,27,7,54,7,2,1,113,21,3,5,3,50,2,4,11,1,12,0]
graph2 = [vertex11, vertex22, vertex33, vertex44,vertex55,vertex66,vertex77,vertex88,vertex99,vertex1010,vertex1111,vertex1212,vertex13,vertex14,vertex15,vertex16,vertex17,vertex18,vertex19,vertex20]