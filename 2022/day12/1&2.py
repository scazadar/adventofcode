#!/usr/bin/env python3
#Imports
import time
import numpy as np
from scipy.sparse.csgraph import shortest_path
import networkx as nx

#Zeit Start
start = time.time()

#Main
f = np.array([[ord(x) for x in [*_.strip()]] for _ in open("inputs/day12").readlines()])

#map = np.pad(map,1)
y,x = np.where(f == ord("S"))
start_position = (y[0],x[0])
f[y,x] = ord('a')
neighbors_to_check = [[y[0],x[0]]]
y,x = np.where(f == ord("E"))
end_position = (y[0],x[0])
print(end_position)
f[y,x] = ord('z')


costs = np.zeros((len(f),len(f[0])))
visited = []

print(f)
while(True):
    y,x = neighbors_to_check.pop()
    if([y,x] not in visited):
        #nach links
        if(x > 0):
            if((f[y,x-1] <= f[y,x] or f[y,x-1] == f[y,x] + 1) and (costs[y,x-1] > costs[y,x] or costs[y,x-1] == 0)):
                costs[y,x-1] = costs[y,x] + 1
                if([y,x-1] not in neighbors_to_check):
                    neighbors_to_check.append([y,x-1])
        #nach rechts
        if(x < len(f[y])-1):
            if((f[y,x+1] <= f[y,x] or f[y,x+1] == f[y,x] + 1) and (costs[y,x+1] > costs[y,x] or costs[y,x+1] == 0)):
                costs[y,x+1] = costs[y,x] + 1
                if([y,x+1] not in neighbors_to_check):
                    neighbors_to_check.append([y,x+1])
        #nach oben
        if(y > 0):
            if((f[y-1,x] <= f[y,x] or f[y-1,x] == f[y,x] + 1) and (costs[y-1,x] > costs[y,x] or costs[y-1,x] == 0)):
                costs[y-1,x] = costs[y,x] + 1
                if([y-1,x] not in neighbors_to_check):
                    neighbors_to_check.append([y-1,x])
        #nach unten
        if(y < len(f)-1):
            if((f[y+1,x] <= f[y,x] or f[y+1,x] == f[y,x] + 1) and (costs[y+1,x] > costs[y,x] or costs[y+1,x] == 0)):
                costs[y+1,x] = costs[y,x] + 1
                if([y+1,x] not in neighbors_to_check):
                    neighbors_to_check.append([y+1,x])
    #visited.append([y,x])

    neighbors_to_check.sort(reverse=True)
    if(len(neighbors_to_check) == 0):
        break
print(costs[end_position[0],end_position[1]])


#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s