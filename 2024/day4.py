#!/usr/bin/env python3
# Imports
import time
import numpy as np

# Zeit Start
start = time.time()

# Main
puzzle = np.array([[n for n in x.strip()] for x in open("2024/inputs/day4").readlines()])

#Part1
xmasCount = 0

def checkXmas(i,s):
    i = "".join(i)
    return i.count(s) + i.count("".join(reversed(s)))

#Horizontal
for r in puzzle:
    xmasCount += checkXmas(r,"XMAS")
#Vertikal
for x in range(len(puzzle[0])):
    xmasCount += checkXmas(puzzle[:,x],"XMAS")
#Diagonal
for x in range((len(puzzle)-1)*-1,len(puzzle[0])-1):
    xmasCount += checkXmas(puzzle.diagonal(x),"XMAS")
    xmasCount += checkXmas(np.fliplr(puzzle).diagonal(x),"XMAS")

print(f"Part1: {xmasCount}")

#Part2
masCount = 0
for x in range(len(puzzle)-2):
    for y in range(len(puzzle[x])-2):
        part = puzzle[x:x+3,y:y+3].copy()
        #X machen
        part[0,1] = "."
        part[1,0] = "."
        part[1,2] = "."
        part[2,1] = "."
        
        masCount += 1 if checkXmas(part.diagonal(),"MAS") and checkXmas(np.fliplr(part).diagonal(),"MAS") else 0
        
print(f"Part2: {masCount}")


# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))

# 0.003s
