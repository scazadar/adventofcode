#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
file = [_ for _ in open("2023/inputs/day11").read().split("\n")]
galaxies = []
emptyroomsy = []
emptyroomsx = []
galaxieConnections = []
distances = []
distancesPart2 = []

for y,line in enumerate(file):
    if(len(line) == line.count(".")):
        emptyroomsy.append(y)
    for x,c in enumerate(line):
        if(c == "#"):
            galaxies.append([y,x])
            
for x in range(len(file[0])):
    if(len([file[_][x] for _ in range(len(file)) if file[_][x] == '.']) == len(file)):
        emptyroomsx.append(x)
            
for x,galaxie1 in enumerate(galaxies):
    for galaxie2 in galaxies[x+1:]:
        galaxieConnections.append([galaxie1,galaxie2])


for _ in galaxieConnections:
    x = abs(_[1][1] - _[0][1])
    y = abs(_[1][0] - _[0][0])

    xPart2 = x
    yPart2 = y
    
    for space in emptyroomsy:
        if(space > _[0][0] and space < _[1][0]):
            y += 1
            yPart2 += 999999
            
    for space in emptyroomsx:
        if(space > _[0][1]  and space < _[1][1] or space < _[0][1] and space > _[1][1]):
            x += 1
            xPart2 += 999999
        
    distances.append(x+y)
    distancesPart2.append(xPart2+yPart2)

    
print(f"Part1: {sum(distances)}")
print(f"Part2: {sum(distancesPart2)}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))