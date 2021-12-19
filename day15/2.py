#!/usr/bin/env python3
import numpy as np
np.set_printoptions(linewidth=200)

f = np.array([[int(_) for _ in _] for _ in [x.strip() for x in open("15.txt").readlines()]])
neighbors_to_check = [[0,0]]

size = len(f)
for _ in range(1,5):
    for x in range(size):
        f = np.insert(f,(size*_)+x,f[:,(size*(_-1)+x)]+1,axis=1)
    f[f>9] = 1
for _ in range(1,5):
    for x in range(size):
        f = np.insert(f,(size*_)+x,f[size*(_-1)+x]+1,axis=0)
    f[f>9] = 1

costs = np.zeros((len(f),len(f[0])))

while(True):
    y,x = neighbors_to_check.pop()
    if(x > 0):
        if(costs[y,x-1] > costs[y,x] + f[y,x-1] or costs[y,x-1] == 0):
            costs[y,x-1] = costs[y,x] + f[y,x-1]
            if([y,x-1] not in neighbors_to_check):
                neighbors_to_check.append([y,x-1])
            
    if(x < len(f[y])-1):
        if(costs[y,x+1] > costs[y,x] + f[y,x+1] or costs[y,x+1] == 0):
            costs[y,x+1] = costs[y,x] + f[y,x+1]
            if([y,x+1] not in neighbors_to_check):
                neighbors_to_check.append([y,x+1])
            
    if(y > 0):
        if(costs[y-1,x] > costs[y,x] + f[y-1,x] or costs[y-1,x] == 0):
            costs[y-1,x] = costs[y,x] + f[y-1,x]
            if([y-1,x] not in neighbors_to_check):
                neighbors_to_check.append([y-1,x])
            
    if(y < len(f)-1):
        if(costs[y+1,x] > costs[y,x] + f[y+1,x] or costs[y+1,x] == 0):
            costs[y+1,x] = costs[y,x] + f[y+1,x]
            if([y+1,x] not in neighbors_to_check):
                neighbors_to_check.append([y+1,x])

    neighbors_to_check.sort(reverse=True)

    if(len(neighbors_to_check) == 0):
        break

print(costs[-1][-1])