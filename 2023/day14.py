#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
platform = [_ for _ in open("2023/inputs/day14.sample").read().split("\n")]

def turnList(l):
    hRows = []
    for x,_ in enumerate(l[0]):
        hRows.append([_[x] for _ in l])
        hRows = ["".join(_) for _ in hRows]
    return hRows

def moveRocks(direction,rocks):
    rocks = [_ for _ in rocks]
    if(direction == 'north' or direction == 'west'):
        for _ in range(1,len(rocks)):
            if(rocks[_-1] == "." and rocks[_] == "O"):
                rocks[_-1] = "O"
                rocks[_] = "."
    if(direction == 'south' or direction == 'east'):
        for _ in range(len(rocks)-1):
            if(rocks[_+1] == "." and rocks[_] == "O"):
                rocks[_+1] = "O"
                rocks[_] = "."
    return "".join(rocks)

def calcLoad(rows):
    load = 0
    for x in range(len(rows),0,-1):
        load += x * rows[len(rows)-x].count("O")
    return load

hRows = turnList(platform)

tempRows = []
while tempRows != hRows:
    tempRows = hRows.copy()
    for x,row in enumerate(hRows):
        hRows[x] = moveRocks("north",row)
    
platform = turnList(hRows)
load = 0
for x in range(len(platform),0,-1):
    load += x * platform[len(platform)-x].count("O")

print(f"Part1: {load}")

# Part 2
platform = [_ for _ in open("2023/inputs/day14").read().split("\n")]
rows = platform.copy()

loads = [rows]
sequence = []
startSequence = 0
endSequence = 0    

for _ in range(1,1000000000):
    tempRows = []
    rows = turnList(rows)
    while tempRows != rows:
        tempRows = rows.copy()
        for x,row in enumerate(rows):
            rows[x] = moveRocks("north",row)
    rows = turnList(rows)
    while tempRows != rows:
        tempRows = rows.copy()
        for x,row in enumerate(rows):
            rows[x] = moveRocks("west",row)
    rows = turnList(rows)
    while tempRows != rows:
        tempRows = rows.copy()
        for x,row in enumerate(rows):
            rows[x] = moveRocks("south",row)
    rows = turnList(rows)
    while tempRows != rows:
        tempRows = rows.copy()
        for x,row in enumerate(rows):
            rows[x] = moveRocks("east",row)
            
    if(rows in loads):
        startSequence = loads.index(rows)
        endSequence = startSequence + (_-startSequence)
        break
    
    loads.append(rows)

print(f"Part2: {calcLoad(loads[(1000000000-startSequence) % (endSequence-startSequence) + startSequence])}")


#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))