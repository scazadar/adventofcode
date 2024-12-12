#!/usr/bin/env python3
# Imports
import time
from collections import Counter

# Zeit Start
start = time.time()

# Main
garden = [[_ for _ in _.strip()]
          for _ in open("2024/inputs/day12.sample").readlines()]
# print(garden)
directions = [(0,1),(1,0),(0,-1),(-1,0)]
regions = {}


def calcFences(y, x):
    c = 0
    if (y-1 < 0 or garden[y-1][x] != garden[y][x]):
        c += 1
    if (y+1 >= len(garden) or garden[y+1][x] != garden[y][x]):
        c += 1
    if (x-1 < 0 or garden[y][x-1] != garden[y][x]):
        c += 1
    if (x+1 >= len(garden[y]) or garden[y][x+1] != garden[y][x]):
        c += 1
    return c


def getNeighbors(coord):
    y, x = coord
    return {(y, x + 1), (y - 1, x), (y, x - 1), (y + 1, x)}

def getNeighborsDiag(coord):
    y, x = coord
    return {
        (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1),
        (y - 1, x - 1), (y - 1, x + 1), (y + 1, x - 1), (y + 1, x + 1)
    }


def findCorners(region):
    print(region)
    corners = 0
    
    # erstmal alle am Rand holen
    edgeElements = [_ for _ in region[0] if sum([1 for neighbor in getNeighborsDiag(_) if neighbor in region[0]]) < 8 ]
    
    direction = 0
    start = edgeElements[0]
    next = ()
    for x in range(4):
        if(tuple((y+x for y,x in zip(edgeElements[0],directions[x % 4]))) in region[0]):
            direction = x
            next = tuple((y+x for y,x in zip(edgeElements[0],directions[x % 4])))
            break
    
    while next != start:
        if(tuple((y+x for y,x in zip(next,directions[direction % 4]))) in region[0]):
            next = tuple((y+x for y,x in zip(next,directions[x % 4])))
            print(next)
        else:
            corners += 1
            for x in range(4):
                
                if(tuple((y+x for y,x in zip(next,directions[direction % 4]))) in region[0]):
                    next = tuple((y+x for y,x in zip(next,directions[direction % 4])))
                    break
    print(corners)




def findRegions(regions):
    visited = set()
    areas = []
    for coord in regions:
        if (coord not in visited):
            visited.add(coord)

            def findNeighbor(area, coord, visited):
                area[0].append(coord)
                area[1] += calcFences(*coord)
                for neighbor in getNeighbors(coord):
                    if (neighbor in regions and neighbor not in visited):
                        visited.add(neighbor)
                        area, visited = findNeighbor(area, neighbor, visited)
                return area, visited

            areas.append(findNeighbor([[], 0], coord, visited)[0])
    return areas


for y, row in enumerate(garden):
    for x, col in enumerate(row):
        if (col in regions):
            regions[col].append((y, x))
        else:
            regions[col] = [(y, x)]

newRegions = []
for _ in regions:
    newRegions.extend(findRegions(regions[_]))


print(f"Part1 : {sum([len(_[0])*_[1] for _ in newRegions])}")


print(findCorners(newRegions[0]))

# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
