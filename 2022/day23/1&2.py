#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
def not_alone(y,x):
    for _ in [[y-1,x],[y-1,x-1],[y-1,x+1],[y+1,x],[y+1,x-1],[y+1,x+1],[y,x-1],[y,x+1]]:
        if(_ in elves):
            return True

def north(y,x):
    if(not [y-1,x] in elves and not [y-1,x-1] in elves and not [y-1,x+1] in elves):
        return [y-1,x]
    else:
        return [y,x]

def south(y,x):
    if(not [y+1,x] in elves and not [y+1,x-1] in elves and not [y+1,x+1] in elves):
        return [y+1,x]
    else:
        return [y,x]

def west(y,x):
    if(not [y,x-1] in elves and not [y-1,x-1] in elves and not [y+1,x-1] in elves):
        return [y,x-1]
    else:
        return [y,x]

def east(y,x):
    if(not [y,x+1] in elves and not [y-1,x+1] in elves and not [y+1,x+1] in elves):
        return [y,x+1]
    else:
        return [y,x]

f = [_.strip() for _ in open("inputs/day23").readlines()]

elves = []

for y in range(len(f)):
    for x in range(len(f[y])):
        if(f[y][x] == '#'):
            elves.append([y,x])

directions = [north,south,west,east]
round = 0

while(True):
    round += 1
    print(round)
    designated_directions = []
    temptime = time.time()
    for elve in elves:
        if(not_alone(*elve)):
            for dir in range(4):
                new_position = directions[dir](*elve)
                if(new_position != elve):
                    designated_directions.append(new_position)
                    break
            else:
                designated_directions.append(elve)
        else:
            designated_directions.append(elve)
    print('Zeit:   {:.3f}s'.format(time.time()-temptime))
    #move
    
    old_elves = elves.copy()
    for x in range(len(designated_directions)):
        if(designated_directions.count(designated_directions[x]) == 1):
            elves[x] = designated_directions[x]
    

    if(old_elves == elves):
        print("Part 2: ", round)
        break
    
    directions.append(directions.pop(0))

    if(round == 10):
        y_lowest= min(_[0] for _ in elves)
        y_highest= max(_[0] for _ in elves)
        x_lowest= min(_[1] for _ in elves)
        x_highest= max(_[1] for _ in elves)
        map = [[y, x ] for x in range(x_lowest,x_highest+1) for y in range(y_lowest,y_highest+1)]
        print("Part 1: ", len([_ for _ in map if _ not in elves]))
    

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s