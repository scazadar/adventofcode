#!/usr/bin/env python3
# Imports
import time

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day19"

towels,designs= open(file).read().split("\n\n")

towels = set([_.strip() for _ in towels.split(",")])
designs = set(designs.split("\n"))

def getNextStrings(current,design):
    new = []
    if not current:
        for towel in towels:
            if(design.startswith(towel)):
                new.append(towel)
    else:
        for c in current:
            for towel in towels:
                if(design.replace(c,"",1).startswith(towel) and len(c+towel) <= len(design) and c+towel not in new):
                    new.append(c + towel)        
    return new

c = 0
for design in designs:
    current = []
    while True:
        current = getNextStrings(current,design)
        if(len(current) == 0):
            break
        elif(design in current):
            c += 1
            break

print(f"Part1: {c}")


#part2
def getNextStrings2(current,design):
    new = []
    if not current:
        for towel in towels:
            if(design.startswith(towel)):
                new.append([towel])
    else:
        for c in current:
            for towel in towels:
                if(design.replace("".join(c),"",1).startswith(towel) and len(c+[towel]) <= len(design) and c+[towel] not in new):
                    new.append(c + [towel])        
    return new

c = 0
possible = []
for design in designs:
    current = []
    while True:
        current = getNextStrings2(current,design)
        if(len(current) == 0):
            break
        elif(design in ["".join(_) for _ in current]):
            c += ["".join(_) for _ in current].count(design)

print(f"Part2: {c}")
        

# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))
