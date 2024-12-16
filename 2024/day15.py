#!/usr/bin/env python3
# Imports
import time
import re
import math

# Zeit Start
start = time.time()

file = "2024/inputs/day15.sample"

warehouse,cmds = [_ for _ in open(file).read().split("\n\n")]
warehouse = [[_ for _ in _] for _ in warehouse.split("\n")]
cmds = cmds.replace("\n","")

def move(cmd, warehouse, cursor):
    directions = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}

    dy, dx = directions[cmd]
    next_row, next_col = cursor[0] + dy, cursor[1] + dx

    if warehouse[next_row][next_col] == 'O':
        warehouse = move(cmd, warehouse, (next_row, next_col))
    
    if warehouse[next_row][next_col] == '.':
        warehouse[next_row][next_col], warehouse[cursor[0]][cursor[1]] = warehouse[cursor[0]][cursor[1]], warehouse[next_row][next_col]
    return warehouse
     
for cmd in cmds:
    robot = [(y,_.index("@")) for y,_ in enumerate(warehouse) if "@" in _][0]
    warehouse = move(cmd,warehouse,robot)
        
gpsc = []
for y,r in enumerate(warehouse):
    for x,_ in enumerate(r):
        if(_ == 'O'):
            gpsc.append((100*y+x))
print(f"Part1: {sum(gpsc)}")
                

#Part2
warehouse,cmds = [_ for _ in open(file).read().split("\n\n")]
warehouse = [[_ for _ in _] for _ in warehouse.split("\n")]
cmds = cmds.replace("\n","")
warehousep2 = []

for yrow in warehouse:
    r = []
    for xrow in yrow:
        if(xrow == '#'):
            r.extend('#' * 2)
        elif(xrow == 'O'):
            r.extend(['[',']'])
        elif(xrow == '.'):
            r.extend('.' * 2)    
        elif(xrow == '@'):
            r.extend(['@','.'])
        else:
            r.extend(xrow)
    warehousep2.append(r)
    
for _ in warehousep2:
    print(_)
    
def move2(cmd, warehouse, cursor):
    directions = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}

    dy, dx = directions[cmd]
    next_row, next_col = cursor[0] + dy, cursor[1] + dx

    print(warehouse[next_row][next_col])

    if warehouse[next_row][next_col] == 'O':
        warehouse = move2(cmd, warehouse, (next_row, next_col))
    
    if warehouse[next_row][next_col] == '.':
        warehouse[next_row][next_col], warehouse[cursor[0]][cursor[1]] = warehouse[cursor[0]][cursor[1]], warehouse[next_row][next_col]
    return warehouse

def move3(cmd,warehouse,cursor):
    if(cmd == ">"):
        wy = warehouse[cursor[0]]
        if(wy[cursor[1] + 1] == 'O'):
            warehouse = move3(cmd,warehouse,(cursor[0],cursor[1]+1))
        if(wy[cursor[1] + 1] == '.'):
            wy[cursor[1] + 1],wy[cursor[1]] = wy[cursor[1]], wy[cursor[1] + 1]
            return warehouse
        elif(wy[cursor[1] + 1] == '#'):
            return warehouse
    elif(cmd == "<"):
        wy = warehouse[cursor[0]]
        if(wy[cursor[1] - 1] == 'O'):
            warehouse = move3(cmd,warehouse,(cursor[0],cursor[1]-1))
        if(wy[cursor[1] - 1] == '.'):
            wy[cursor[1] - 1],wy[cursor[1]] = wy[cursor[1]], wy[cursor[1] - 1]
            return warehouse
        elif(wy[cursor[1] - 1] == '#'):
            return warehouse
    elif(cmd == "v"):
        if(warehouse[cursor[0] + 1][cursor[1]] == 'O'):
            warehouse = move3(cmd,warehouse,(cursor[0]+1,cursor[1]))
        if(warehouse[cursor[0] + 1][cursor[1]] == '.'):
            warehouse[cursor[0] + 1][cursor[1]],warehouse[cursor[0]][cursor[1]] = warehouse[cursor[0]][cursor[1]], warehouse[cursor[0] + 1][cursor[1]]
            return warehouse
        elif(warehouse[cursor[0] + 1][cursor[1]] == '#'):
            return warehouse
    elif(cmd == "^"):
        if(warehouse[cursor[0] - 1][cursor[1]] == 'O'):
            warehouse = move3(cmd,warehouse,(cursor[0]-1,cursor[1]))
        if(warehouse[cursor[0] - 1][cursor[1]] == '.'):
            warehouse[cursor[0] - 1][cursor[1]],warehouse[cursor[0]][cursor[1]] = warehouse[cursor[0]][cursor[1]], warehouse[cursor[0] - 1][cursor[1]]
            return warehouse
        elif(warehouse[cursor[0] - 1][cursor[1]] == '#'):
            return warehouse 
    return warehouse
     
for cmd in cmds:
    robot = [(y,_.index("@")) for y,_ in enumerate(warehouse) if "@" in _][0]
    warehouse = move3(cmd,warehousep2,robot)
        
gpsc = []
for y,r in enumerate(warehouse):
    for x,_ in enumerate(r):
        if(_ == 'O'):
            gpsc.append((100*y+x))
print(f"Part1: {sum(gpsc)}")
    
    
    
    

        
            
    

        
    
        
        
    



# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
