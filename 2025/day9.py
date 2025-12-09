#!/usr/bin/env python3
#Imports
import time
from shapely.geometry import Polygon
from shapely import box
import matplotlib.pyplot as plt

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

poly = Polygon(grid)

""" fig, ax = plt.subplots()
x, y = poly.exterior.xy
ax.plot(x, y, color="black")
ax.grid(True, linestyle=":", linewidth=0.5)
ax.set_aspect("equal")
ax.invert_yaxis()   
plt.show()  """

retangles = []
for i,tile1 in enumerate(grid):
    for tile2 in grid[i+1:]:
        x = abs(tile1[0] - tile2[0])+1
        y = abs(tile1[1] - tile2[1])+1
        rect = box(*tile1,*tile2) 

        if(poly.contains(rect)):
            retangles.append((x,y)) 

print(f"Part 2: {max([_[0]*_[1] for _ in retangles])}")        
    

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))