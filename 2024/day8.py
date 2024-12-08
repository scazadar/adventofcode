#!/usr/bin/env python3
# Imports
import time
from itertools import combinations

# Zeit Start
start = time.time()

# Main
map = [[_ for _ in _.strip()] for _ in open("2024/inputs/day8").readlines()]

def abstand(p1,p2):
    return [abs(p2[0]-p1[0]),abs(p2[1]-p1[1])]

antennas = {}
for y,r in enumerate(map):
    for x,c in enumerate(r):
        if(c != "."):
            if(c in antennas.keys()):
                antennas.get(c)[0].append((y,x))
            else:
                antennas.setdefault(c,[[(y,x)],[]])
                
def calcAntinodes(p1,p2,d):
        an1 = [0,0]
        an2 = [0,0]
        #y
        if(p1[0] < p2[0]):
            an1[0] = p1[0] - d[0]
            an2[0] = p2[0] + d[0]
        elif(p1[0] > p2[0]):
            an1[0] = p1[0] + d[0]
            an2[0] = p2[0] - d[0]
        else:
            an1[0] = p1[0]
            an2[0] = p1[0]
        #x
        if(p1[1] < p2[1]):
            an1[1] = p1[1] - d[1]
            an2[1] = p2[1] + d[1]
        elif(p1[1] > p2[1]):
            an1[1] = p1[1] + d[1]
            an2[1] = p2[1] - d[1]
        else:
            an1[1] = p1[1]
            an2[1] = p1[1]
            
        return an1,an2
    
#Part1
antinodes = []
for frequency in antennas:
    for p1, p2 in combinations(antennas.get(frequency)[0],2):
        for an in calcAntinodes(p1,p2,abstand(p1,p2)):
            if(an[0] >= 0 and an[0] < len(map) and an[1] >= 0 and an[1] < len(map[0])):
                antinodes.append(an)
            
print(f"Part1: {len(set([f"{_[0]},{_[1]}" for _ in antinodes]))}")

#Part2
for frequency in antennas:
    for p1, p2 in combinations(antennas.get(frequency)[0],2):
        antinodes.extend([p1,p2])
        bothOut = False
        d = abstand(p1,p2)
        while bothOut == False:
            p1,p2 = calcAntinodes(p1,p2,d)
            outCount = 0
            for an in [p1,p2]:
                if(an[0] >= 0 and an[0] < len(map) and an[1] >= 0 and an[1] < len(map[0])):
                    antinodes.append(an)
                else:
                    outCount += 1           
            bothOut = True if outCount == 2 else False
                      
print(f"Part2: {len(set([f"{_[0]},{_[1]}" for _ in antinodes]))}")


# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))