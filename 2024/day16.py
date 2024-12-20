#!/usr/bin/env python3
# Imports
import time

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day16.sample"

maze = [_.strip() for _ in open(file).readlines()]
directions = ((0,1),(1,0),(0,-1),(-1,0))
visitedWithCosts = {}

def getNextCursors(path):
    cursor = path[0][-1]

    newPaths = []
    for d in directions:
        dy, dx = d
        next_y, next_x = cursor[0] + dy, cursor[1] + dx
        costs = path[1]
        if(maze[next_y][next_x] in ['.','E'] and (next_y,next_x) not in path[0]):
            oldDirection = path[2]
            if(oldDirection == d):
                costs += 1
            elif(directions[(directions.index(oldDirection) + 1) % 4] == d or directions[(directions.index(oldDirection) - 1) % 4] == d):
                costs += 1001
            else:
                costs += 2001
            
            if((next_y,next_x) not in visitedWithCosts or costs < visitedWithCosts[(next_y,next_x)]):
                visitedWithCosts[(next_y,next_x)] = costs
                newPaths.append([path[0] + [(next_y,next_x)],costs,d])
    return newPaths

start = [(y,_.index('S')) for y,_ in enumerate(maze) if 'S' in _][0]
end = [(y,_.index('E')) for y,_ in enumerate(maze) if 'E' in _][0]

#Part1
paths = [[[start],0,(0,1)]]
visitedWithCosts = {}
visitedWithCosts[start] = 0
finished = []
while True:
    newPaths = []
    for path in paths:
        print(path)
        nextPaths = getNextCursors(path)
        for p in nextPaths:
            if(end == p[0][-1]):
                finished.append(p)
            else:
                newPaths.extend(nextPaths)
    if(len(newPaths) == 0):
        break
    paths = newPaths
    
minCosts = min([_[1] for _ in finished])
print(f"Part1: {minCosts}")


count = 0
for f in finished:
    if(f[1] == min([_[1] for _ in finished])):
        count+=1
            
print(count)

# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))
