#!/usr/bin/env python3
# Imports
import time

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day18"

bytes = [tuple(int(_) for _ in _.strip().split(",")) for _ in open(file).readlines()]

directions = ((0,1),(1,0),(0,-1),(-1,0))
visitedWithCosts = {}

mspacey,mspacex = 71,71
bytesToDrop = 1024

#mspacey,mspacex = 7,7
#bytesToDrop = 12

memory = [["." for _ in range(mspacex)] for _ in range(mspacey)]
memoryP2 = [["." for _ in range(mspacex)] for _ in range(mspacey)]

#print(bytes)
#print(memory)

def getNextCursors(path,memory):
    cursor = path[0][-1]

    newPaths = []
    for d in directions:
        dy, dx = d
        next_y, next_x = cursor[0] + dy, cursor[1] + dx
        costs = path[1]
        if(0 <= next_y < len(memory) and 0 <= next_x < len(memory[0]) and memory[next_y][next_x] in ['.'] and (next_y,next_x) not in path[0]):
            costs += 1    
                    
            if((next_y,next_x) not in visitedWithCosts or costs < visitedWithCosts[(next_y,next_x)]):
                visitedWithCosts[(next_y,next_x)] = costs
                newPaths.append([path[0] + [(next_y,next_x)],costs,d])
    return newPaths

def dropBytes(memory,s,c):
    for byte in bytes[:c]:
        memory[byte[1]][byte[0]] = '#'
        
def calcPaths(memory):
    finished = []
    paths = [[[(0,0)],0]]
    while True:
        newPaths = []
        for path in paths:
            nextPaths = getNextCursors(path,memory)
            for p in nextPaths:
                if((len(memory)-1,len(memory[0])-1) == p[0][-1]):
                    finished.append(p)
                else:
                    newPaths.extend(nextPaths)
        if(len(newPaths) == 0):
            break
        paths = newPaths
    return finished


dropBytes(memory,0,bytesToDrop)
minCosts = min([_[1] for _ in calcPaths(memory)])
print(f"Part1: {minCosts}")

#Part2
for n in range(1,len(bytes)):
    visitedWithCosts = {}
    dropBytes(memoryP2,0,n)
    f = calcPaths(memoryP2)
    if(len(f) == 0):
        print(f"Part2: {",".join([str(_) for _ in bytes[n-1]])}")
        break

# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))
