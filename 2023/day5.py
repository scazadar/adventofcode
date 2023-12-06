#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

pointSum:int = 0
winNumberList:list = []

#Main
def getDestination(source:int,mapName:str,destinationMap:dict):
    path = []
  
    destination:int = source
    for m in destinationMap:
        if(source >= m[1] and source < m[1]+m[2]):
            destination = source + m[0] - m[1]
    path.append(destination)

    if(mapName.split("-to-")[1] != "location"):
        path += getDestination(destination,findKey(mapName.split("-to-")[1]),maps.get(findKey(mapName.split("-to-")[1])))        
 
    return path
    
    
def findKey(key:str):
    for k in maps:
        if(k.startswith(key)):
            return k

almanac:list = [page for page in open("2023/inputs/day5").read().split("\n")]
seeds:list = [int(x) for x in almanac[0].split(" ")[1:]]
maps:dict = {}

almanac_entry:list = []
for row in almanac[2:]:
    if(row == ''):
        maps.setdefault(almanac_entry[0].split(" ")[0],[[int(x) for x in i.split(" ")] for i in almanac_entry[1:]])
        almanac_entry = []
    else:
        almanac_entry.append(row)
maps.setdefault(almanac_entry[0].split(" ")[0],[[int(x) for x in i.split(" ")] for i in almanac_entry[1:]])

paths = []
for seed in seeds:
    paths.append(getDestination(seed,findKey("seed"),maps.get(findKey("seed"))))
    

print(f"Part1: {min([x[-1] for x in paths])}")

#Part 2
seedRange:list = []

x = 0
seedPair:list = []
for seed in seeds:
    seedPair.append(seed)
    if(x == 1):
        seedRange.append(range(seedPair[0],seedPair[0]+seedPair[1]))
        x = 0
        seedPair = []
    else:
        x += 1

paths = []
for range in seedRange:
    for seed in range:
        paths.append(getDestination(seed,findKey("seed"),maps.get(findKey("seed")))[-1])
        paths = [min(paths)]
    print(paths)
    
print(f"Part2: {min(paths)}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))