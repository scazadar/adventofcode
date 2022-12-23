#!/usr/bin/env python3
#Imports
import time
import numpy as np

#Zeit Start
start = time.time()

#Main

def check_sides(cube):
    connected_sides = 0
    if([cube[0] + 1, cube[1], cube[2] ] in f):
        connected_sides += 1
    if([cube[0] - 1, cube[1], cube[2] ] in f):
        connected_sides += 1
    if([cube[0], cube[1] + 1, cube[2] ] in f):
        connected_sides += 1
    if([cube[0], cube[1] - 1, cube[2] ] in f):
        connected_sides += 1
    if([cube[0], cube[1], cube[2] + 1 ] in f):
        connected_sides += 1
    if([cube[0], cube[1], cube[2] - 1 ] in f):
        connected_sides += 1
    return connected_sides

def check_air(cube):
    print(lava[cube[2],cube[1],:cube[0]])
    if(1 in lava[cube[2],cube[1],:cube[0]] and 1 in lava[cube[2],cube[1],cube[0]:] and 1 in lava[cube[2],cube[1]:,cube[0]] and 1 in lava[cube[2],:cube[1],cube[0]] and 1 in lava[cube[2]:,cube[1],cube[0]] and 1 in lava[:cube[2],cube[1],cube[0]]):
        return True

f = [list(map(int,_.strip().split(","))) for _ in open("inputs/day18.sample").readlines()]

not_connected_sides = 0

# Part 2
max_x = max(_[0] for _ in f)
max_y = max(_[1] for _ in f)
max_z = max(_[2] for _ in f)

lava = np.zeros((max_z,max_y,max_x))
#####


for cube in f:
    lava[cube[2]-1,cube[1]-1,cube[0]-1] = 1
    not_connected_sides += (6 - check_sides(cube))

print("Part 1: ", not_connected_sides)

edge = False

exterior_surface = 0

air = []

for z in range(max_z):
    for y in range(max_y):
        for x in range(max_x):
            if(lava[z,y,x] == 1):
                exterior_surface += 1
                break
        for x in reversed(range(max_x)):
            if(lava[z,y,x] == 1):
                exterior_surface += 1
                break
            

for z in range(max_z):
    for x in range(max_x):
        for y in range(max_y):
            if(lava[z,y,x] == 1):
                exterior_surface += 1
                break
        for y in reversed(range(max_y)):
            if(lava[z,y,x] == 1):
                exterior_surface += 1
                break

for x in range(max_x):
    for y in range(max_y):
        for z in range(max_z):
            if(lava[z,y,x] == 1):
                exterior_surface += 1
                break
        for z in reversed(range(max_z)):
            if(lava[z,y,x] == 1):
                exterior_surface += 1
                break

print("Part 2: ", exterior_surface)


np.set_printoptions(threshold=np.inf)

#print(lava[:,1,1])
#print("####")
print(lava)

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s