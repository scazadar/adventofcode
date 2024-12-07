#!/usr/bin/env python3
# Imports
import time, copy

# Zeit Start
start = time.time()

# Main
map = [[_ for _ in _.strip()] for _ in open("2024/inputs/day6").readlines()]
directions = [(-1,0),(0,1),(1,0),(0,-1)]

def calcVisited(map,startPosition,currentDirection,oldVisited=[]):
    currentPosition = startPosition.copy()
    visited = []
    visitedDirection = []
    
    while True:
        nextPosition = [y+x for y,x in zip(currentPosition,directions[currentDirection % 4])]

        if(nextPosition[0] < 0 or nextPosition[0] >= len(map) or nextPosition[1] < 0 or nextPosition[1] >= len(map[0])):
            visited.append(currentPosition)
            visitedDirection.append((currentDirection % 4,*currentPosition))
            break
        elif(map[nextPosition[0]][nextPosition[1]] == '#'):
            currentDirection += 1
        else:
            if((currentDirection % 4,*nextPosition) in visitedDirection):
                return False    
            
            visited.append(currentPosition)
            visitedDirection.append((currentDirection % 4,*currentPosition))
   
            currentPosition = nextPosition
    
    return visited,visitedDirection

currentDirection = 0
startPosition = [0,0]

for y,_ in enumerate(map):
    for x,_ in enumerate(_):
        if(_ in ["^",">","<","v"]):
            startPosition = [y,x]
            currentDirection = ["^",">","<","v"].index(_)

print(startPosition,currentDirection)

visited,path = calcVisited(map,startPosition,currentDirection)

print(f"Part1: {len(set([f"{_[0]},{_[1]}" for _ in visited]))}")

# Part2
c = []

for i,p in enumerate(path):
    mmap = copy.deepcopy(map)    
    mmap[p[1]][p[2]] = '#'
    
    if((p[1],p[2]) not in c):
        if(calcVisited(mmap,startPosition,currentDirection,path) == False):
            #c += 1
            c.append((p[1],p[2]))
            print(len(set(c)))
            
print(f"Part2: {len(set(c))}") 


# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))