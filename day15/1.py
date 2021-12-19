#!/usr/bin/env python3
import numpy as np

f = np.array([[int(_) for _ in _] for _ in [x.strip() for x in open("15.txt").readlines()]])
costs = np.zeros((len(f),len(f[0])))
neighbors_to_check = [[0,0]]


def checkNeighbors(y=0,x=0):
    neighbors = []
    if(x > 0):
        if(costs[y,x-1] > costs[y,x] + f[y,x-1] or costs[y,x-1] == 0):
            costs[y,x-1] = costs[y,x] + f[y,x-1]
            neighbors.append([y,x-1])
            
    if(x < len(f[y])-1):
        if(costs[y,x+1] > costs[y,x] + f[y,x+1] or costs[y,x+1] == 0):
            costs[y,x+1] = costs[y,x] + f[y,x+1]
            neighbors.append([y,x+1])
            
    if(y > 0):
        if(costs[y-1,x] > costs[y,x] + f[y-1,x] or costs[y-1,x] == 0):
            costs[y-1,x] = costs[y,x] + f[y-1,x]
            neighbors.append([y-1,x])
            
    if(y < len(f)-1):
        if(costs[y+1,x] > costs[y,x] + f[y+1,x] or costs[y+1,x] == 0):
            costs[y+1,x] = costs[y,x] + f[y+1,x]
            neighbors.append([y+1,x])
    return neighbors

while(True):
    y,x = neighbors_to_check.pop()
    neighbors_to_check = neighbors_to_check + checkNeighbors(y,x)
    neighbors_to_check.sort(reverse=True)

    if(len(neighbors_to_check) == 0):
        break

print(costs[-1][-1])