#!/usr/bin/env python3
# Imports
import time
from itertools import combinations

# Zeit Start
start = time.time()

# Main
mountain = [[int(_) for _ in _.strip()] for _ in open("2024/inputs/day10").readlines()]

ways = []
def nextStep(y,x):
    nextSteps = []
    if(y - 1 >= 0 and mountain[y-1][x] == mountain[y][x] + 1):
        nextSteps.append((y-1,x))
    if(x - 1 >= 0 and mountain[y][x-1] == mountain[y][x] + 1):
        nextSteps.append((y,x-1))
    if(y + 1 < len(mountain) and mountain[y+1][x] == mountain[y][x] + 1):
        nextSteps.append((y+1,x))
    if(x + 1 < len(mountain[x]) and mountain[y][x+1] == mountain[y][x] + 1):
        nextSteps.append((y,x+1))
    return list(set(nextSteps))

for y,r in enumerate(mountain):
    for x,c in enumerate(r):
        if(c == 0):
            ways.append([(y,x),[(y,x)]])

for step in range(9):
    for way in ways:
        nextPositions = []
        for position in way[1]:
            nextPositions.extend(nextStep(position[0],position[1]))
        way[1] = nextPositions

print(f"Part1: {sum([len(set(_[1])) for _ in ways])}")
print(f"Part2: {sum([len(_[1]) for _ in ways])}")

# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))