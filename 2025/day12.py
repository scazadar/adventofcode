#!/usr/bin/env python3
#Imports
import time, re, sys
from functools import cache

#Zeit Start
start = time.time()

#Main

#Part 1
input = [r for r in open("inputs/day12").read().split("\n\n")]
presentShapes = [tuple(tuple(1 if _ == '#' else 0 for _ in _ ) for _ in _[2:].strip().split("\n")) for _ in input[:-1]]
sizes = [tuple([tuple(map(int,_.split(":")[0].split("x"))),tuple(map(int,_.split(":")[1].split()))]) for _ in input[-1].split("\n")]

@cache
def countParts(presentShape):
    return sum([_.count(1) for _ in presentShape])

def calcSize(grid, presents):
    n = grid[0] * grid[1]
    all = sum([c*countParts(presentShapes[i]) for i,c in enumerate(presents)])
    return n > all
    
reducedPresentShapes = []

for grid in sizes:
    if(calcSize(grid[0],grid[1])):
        reducedPresentShapes.append(tuple([grid[0],grid[1]]))
    
print(f"Part 1: {len(reducedPresentShapes)}")


   
    

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))