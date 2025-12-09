#!/usr/bin/env python3
#Imports
import time, math

#Zeit Start
start = time.time()

#Main
grid = [tuple(map(int,n.strip().split(","))) for n in open("inputs/day9").readlines()]

retangles = []
for i,tile1 in enumerate(grid):
    for tile2 in grid[i+1:]:
        x = abs(tile1[0] - tile2[0])+1
        y = abs(tile1[1] - tile2[1])+1
        retangles.append((x,y))
        
print(f"Part 1: {max([_[0]*_[1] for _ in retangles])}")

""" allPointsOnLine = []
for i,tile in enumerate(grid):
    if(i+1 < len(grid)):
        nextTile = grid[i+1] 
    else:
        nextTile = grid[0]
    
    if(tile[0] == nextTile[0]):
        tiles = []
        if(tile[1] < nextTile[1]):
            tiles = [(tile[0],_) for _ in range(tile[1],nextTile[1])]
        else:
            tiles = [(tile[0],_) for _ in range(tile[1],nextTile[1]-1,-1)]
        allPointsOnLine.extend(tiles)
    elif(tile[1] == nextTile[1]):
        tiles = []
        if(tile[0] < nextTile[0]):
            tiles = [(_, tile[1]) for _ in range(tile[0],nextTile[0])]
        else:
            tiles = [(_, tile[1]) for _ in range(tile[0],nextTile[0]-1,-1)]
        allPointsOnLine.extend(tiles) """
        
    
retangles = []
for i,tile in enumerate(grid[2:]):
    pass

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))