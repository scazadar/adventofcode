#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
sketch = [_ for _ in open("2023/inputs/day10").read().split("\n")]
symbols = "S|-LJ7F"

sketch = [f"..{_}.." for _ in sketch]
sketch.insert(0,"." * len(sketch[0]))
sketch.insert(0,"." * len(sketch[0]))
sketch.insert(len(sketch[0]),"." * len(sketch[0]))
sketch.insert(len(sketch[0]),"." * len(sketch[0]))
sketch = [[_ for _ in _] for _ in sketch]

sketchcopy = sketch.copy()

startPosition = [0,0]
lastPosition = [0,0]
cursor = []
pathLength = 0

for y,l in enumerate(sketch):
    for x,s in enumerate(sketch[y]):
        if(s == "S"):
            cursor = [x,y]
            break
        
startPosition = cursor
lastPosition = cursor

loopparts = [[cursor[0],cursor[1]]]

#Erste Pipe nach Start finden
if(sketch[cursor[1]+1][cursor[0]] in symbols):
    cursor = [cursor[0],cursor[1]+1]
elif(sketch[cursor[1]][cursor[0]+1] in symbols):
    cursor = [cursor[0]+1,cursor[1]]
elif(sketch[cursor[1]-1][cursor[0]] in symbols):
    cursor = [cursor[0],cursor[1]-1]
elif(sketch[cursor[1]][cursor[0]-1] in symbols):
    cursor = [cursor[0]-1,cursor[1]]
    
while cursor != startPosition:
    loopparts.append([cursor[0],cursor[1]])
    pathLength += 1
    t = cursor
    if(sketch[cursor[1]][cursor[0]] == "L"):
        cursor = [cursor[0]+1,cursor[1]] if [cursor[0]+1,cursor[1]] != lastPosition else [cursor[0],cursor[1]-1]
    elif(sketch[cursor[1]][cursor[0]] == "J"):
        cursor = [cursor[0],cursor[1]-1] if [cursor[0],cursor[1]-1] != lastPosition else [cursor[0]-1,cursor[1]]
    elif(sketch[cursor[1]][cursor[0]] == "7"):
        cursor = [cursor[0]-1,cursor[1]] if [cursor[0]-1,cursor[1]] != lastPosition else [cursor[0],cursor[1]+1]
    elif(sketch[cursor[1]][cursor[0]] == "F"):
        cursor = [cursor[0]+1,cursor[1]] if [cursor[0]+1,cursor[1]] != lastPosition else [cursor[0],cursor[1]+1]
    elif(sketch[cursor[1]][cursor[0]] == "|"):
        cursor = [cursor[0],cursor[1]+1] if [cursor[0],cursor[1]+1] != lastPosition else [cursor[0],cursor[1]-1]
    elif(sketch[cursor[1]][cursor[0]] == "-"):
        cursor = [cursor[0]+1,cursor[1]] if [cursor[0]+1,cursor[1]] != lastPosition else [cursor[0]-1,cursor[1]]
    lastPosition = t
    
print(f"Part1: {int(pathLength/2+1)}")

# Part2   
inside =[]
templist = []
outside = []
oldTemplist = []
for y in range(1,len(sketch)-1):
    for x in range(1,len(sketch[y])-1):
        left = "".join([sketch[y][_] for _ in range(len(sketch[y][:x])) if [_,y] in loopparts and sketch[y][_] != "-"])
        right = "".join([sketch[y][_+x] for _ in range(len(sketch[y][x+1:])) if [_+x,y] in loopparts and sketch[y][_+x] != "-"])
        up = "".join([_ for _ in [sketch[_][x]  for _ in range(len(sketch[:y])) if [x,_] in loopparts and sketch[_][x] != "|"]])
        down = "".join([_ for _ in [sketch[_+y][x]  for _ in range(len(sketch[y+1:])) if [x,_+y] in loopparts and sketch[_+y][x] != "|"]])
        
        if([x,y] not in loopparts
           and ("L7" in left or "FJ" in left or left.count("|") % 2 == 1)
           and ("L7" in right or "FJ" in right or right.count("|") % 2 == 1)
           and ("7L" in up or "FJ" in up or up.count("-") % 2 == 1)
           and ("7L" in down or "FJ" in down or down.count("-") % 2 == 1)
           #and len([sketch[y][_] for _ in range(len(sketch[y][:x])) if [_,y] in loopparts]) > 0
           #and len([sketch[y][_+x] for _ in range(len(sketch[y][x+1:])) if [_+x,y] in loopparts]) > 0
           #and len([_ for _ in [sketch[_][x]  for _ in range(len(sketch[:y])) if [x,_] in loopparts]]) > 0
           #and len([_ for _ in [sketch[_+y][x]  for _ in range(len(sketch[y+1:])) if [x,_+y] in loopparts]]) > 0
           ):
            inside.append([x,y])  
            sketchcopy[y][x] = 'I'
        elif([x,y] not in loopparts):
            sketchcopy[y][x] = 'O'

for _ in sketchcopy:
    print("".join(_))  
            
        
print(inside)
print(f"Part2: {len(inside)}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))