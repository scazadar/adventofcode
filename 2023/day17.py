#!/usr/bin/env python3
#Imports
import time
from collections import deque

#Zeit Start
start = time.time()

#Main
f = [[int(_) for _ in _] for _ in open("2023/inputs/day17.sample").read().split("\n")]


paths = {}
s = (0,0)
checked = []

def getNextNode(node):
    heatLoss = 0
    nodes = []
    if(node != (len(f[0])-1,len(f)-1)):
        if(node[0] > 0):
            if((node,(node[0]-1,node[1])) not in checked):
                checked.append((node,(node[0]-1,node[1])))
                nodes.append(getNextNode((node[0]-1,node[1])))
                #if(nextPath[2] < node[2]):
                #    node[2] = nextPath[2]
        if(node[0] < len(f[0])-1):
            if((node,(node[0]+1,node[1])) not in checked):
                checked.append((node,(node[0]+1,node[1])))
                nodes.append(getNextNode((node[0]+1,node[1])))
                #if(nextPath[2] < node[2]):
                #    node[2] = nextPath[2]
        if(node[1] > 0):
            if((node,(node[0],node[1]-1)) not in checked):
                checked.append((node,(node[0],node[1]-1)))
                nodes.append(getNextNode((node[0],node[1]-1)))
                #if(nextPath[2] < node[2]):
                #    node[2] = nextPath[2]
        if(node[1] < len(f)-1):
            if((node,(node[0],node[1]+1)) not in checked):
                checked.append((node,(node[0],node[1]+1)))
                nodes.append(getNextNode((node[0],node[1]+1)))
                #if(nextPath[2] < node[2]):
                #    node[2] = nextPath[2]
    
    print("---")
    print(nodes)
    print(node)
    if(len(nodes) > 0):
        heatLoss = f[node[1]][node[0]] + min(nodes)
    else:
        heatLoss = f[node[1]][node[0]]
        
    print(heatLoss)
    print("return")
    return heatLoss
    
print(getNextNode((0,0)))



#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))