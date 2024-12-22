#!/usr/bin/env python3
# Imports
import time
import functools

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day20"

racetrack = [[_ for _ in _.strip()] for _ in open(file).readlines()]

start = [(y,_.index('S')) for y,_ in enumerate(racetrack) if 'S' in _][0]
end = [(y,_.index('E')) for y,_ in enumerate(racetrack) if 'E' in _][0]

def getNextCursors(path,m,visitedWithCosts):
    directions = ((0,1),(1,0),(0,-1),(-1,0))
    cursor = path[0][-1]

    newPaths = []
    for d in directions:
        dy, dx = d
        next_y, next_x = cursor[0] + dy, cursor[1] + dx
        costs = path[1]
        if(0 <= next_y < len(m) and 0 <= next_x < len(m[0]) and m[next_y][next_x] in ['.','E'] and (next_y,next_x) not in path[0]):
            costs += 1    
            if((next_y,next_x) not in visitedWithCosts or costs < visitedWithCosts[(next_y,next_x)]):
                visitedWithCosts[(next_y,next_x)] = costs
                newPaths.append([path[0] + [(next_y,next_x)],costs])
    return newPaths,visitedWithCosts

def getPath(m):
    finished = []
    visitedWithCosts = {}
    paths = [[[start],0]]
    while True:
        newPaths = []
        for path in paths:
            nextPaths,visitedWithCosts = getNextCursors(path,m,visitedWithCosts)
            for p in nextPaths:
                if(p[0][-1] == end):
                    finished.append(p)
                else:
                    newPaths.extend(nextPaths)
        if(len(newPaths) == 0):
            break
        paths = newPaths
    return finished

racePath = getPath(racetrack)[0]
racePathLength = racePath[1]

#Part1
cheatPathLengths = []
for n,position in enumerate(racePath[0]):
    directions = ((0,2),(2,0),(0,-2),(-2,0))
    for d in directions:
        dy, dx = d
        next_y, next_x = position[0] + dy, position[1] + dx
        if((next_y,next_x) in racePath[0] and racePath[0].index((next_y,next_x)) > n and (racePath[0].index((next_y,next_x)) - n - 2) != 0):
            cheatPathLengths.append((racePath[0].index((next_y,next_x)) - n - 2))

print(f"Part1: {len(list(filter(lambda x: x >= 100, cheatPathLengths)))}")
    

#Part2 (damit geht auch Part1)
# #Kreis
@functools.cache
def getCircle(radius,point):
    centery, centerx = point
    points_inside_circle = []

    for y in range(len(racetrack)):
        for x in range(len(racetrack[0])):
            if (y - centery)**2 + (x - centerx)**2 <= radius**2:
                points_inside_circle.append((y, x))
    return points_inside_circle

def getCheatPaths(r,racePath):
    cheatPathLengths = {}
    for n,position in enumerate(racePath[0]):
        cheatPathLengths[position] = []
        for d in list(set(getCircle(r,position)) & set(racePath[0])):
        #for d in racePath[0][n:]:
            next_y, next_x = d
            # #Manhattan-Metrik https://de.wikipedia.org/wiki/Manhattan-Metrik
            i = abs(next_y - position[0]) + abs(next_x - position[1])    
            if((next_y,next_x) in racePath[0] and racePath[0].index((next_y,next_x)) > n and (racePath[0].index((next_y,next_x)) - n - i) != 0 and i <= r):
                cheatPathLengths[position].append((racePath[0].index((next_y,next_x)) - n - i))
    return cheatPathLengths

cheatPaths = getCheatPaths(20,racePath)
print(f"Part2: {len(list(filter(lambda x: x >= 100, sum([cheatPaths[_] for _ in cheatPaths], []))))}")


# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))
