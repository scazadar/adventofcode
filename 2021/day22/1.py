#!/usr/bin/env python3
import numpy as np

input = [[_.split(",") for _ in x.strip().split(" ")] for x in open("22.txt").readlines()]

commands = []
for _ in input:
    commands.append([[_[0][0],[[int(_)+50 for _ in _.split("=")[1].split("..")] for _ in _[1]]]][0])

cubes = np.zeros((101,101,101))

for command in commands:
    if(command[0] == 'on'):
        cubes[command[1][0][0]:command[1][0][1]+1,command[1][1][0]:command[1][1][1]+1,command[1][2][0]:command[1][2][1]+1] = 1
    if(command[0] == 'off'):
        cubes[command[1][0][0]:command[1][0][1]+1,command[1][1][0]:command[1][1][1]+1,command[1][2][0]:command[1][2][1]+1] = 0

print(np.count_nonzero(cubes))