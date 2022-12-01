#!/usr/bin/env python3
input = [[int(_) for _ in _[1].replace(",","").split("..")] for _ in [_.split("=") for _ in [x.strip() for x in open("17.txt").readlines()][0].split()[2:]]]

print(input)
paths = []

max_x_velocity = max(input[0])
min_y_velocity = min(input[1])

def probe(x_velocity,y_velocity):
    path = []
    x,y = 0,0
    while(True):
        if(x > input[0][1] or y < input[1][0]):
            break        
        path.append([x,y])
        x += x_velocity
        y += y_velocity
        if(x_velocity > 0):
            x_velocity -= 1
        y_velocity -= 1
    return path

probes = []
for x_velocity in range(0,max_x_velocity+1):
    for y_velocity in range(min_y_velocity,abs(min_y_velocity)+1):   
        path = probe(x_velocity,y_velocity)
        x = path[-1][0]
        y = path[-1][1]
        if(x >= input[0][0] and x <= input[0][1] and y >= input[1][0] and y <= input[1][1]):
            probes.append(path)

highest_y = 0
for _ in probes:
    highest = max([_[1] for _ in _])
    if(highest > highest_y):
        highest_y = highest


print(f"Part1: {highest_y}")
print(f"Part2: {len(probes)}")