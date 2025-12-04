#!/usr/bin/env python3
#Imports
import time, re, sys, copy

#Zeit Start
start = time.time()

#Main
def getNeighbors(coord,grid):
    y, x = coord
    neighbors = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1),
        (y - 1, x - 1), (y - 1, x + 1), (y + 1, x - 1), (y + 1, x + 1)]
    validNeighbors = []
    for yi,xi in neighbors:
        if(0 <= yi < len(grid) and 0 <= xi < len(grid[0])):
            validNeighbors.append((yi,xi))
    return validNeighbors
    
""" 
vllt brauche ich das mal. aber hier doch nicht
def addEdges(c):
    for _ in range(4):
        c.append(["." for _ in range(len(c[0]))])
        c = list(zip(*c[::-1]))
    return c """

department = [[_ for _ in s.strip()] for s in open("inputs/day4").readlines()]

accessablePaper = 0

for y,row in enumerate(department):
    for x,c in enumerate(department):
        if(department[y][x] == "@"):
            adjacentPapers = [department[coord[0]][coord[1]] for coord in getNeighbors([y,x],department)]
            if(adjacentPapers.count("@") < 4):
                accessablePaper += 1     
print(f"Part 1: {accessablePaper}")

accessablePaper = 0
while True:
    oldaccessablePaper = accessablePaper
    for y,row in enumerate(department):
        for x,c in enumerate(department):
            if(department[y][x] == "@"):
                adjacentPapers = [department[coord[0]][coord[1]] for coord in getNeighbors([y,x],department)]
                if(adjacentPapers.count("@") < 4):
                    accessablePaper += 1
                    department[y][x] = "."
    if (oldaccessablePaper == accessablePaper):
        break
print(f"Part 2: {accessablePaper}")
                    

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))