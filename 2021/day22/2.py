#!/usr/bin/env python3
import numpy as np

input = [[_.split(",") for _ in x.strip().split(" ")] for x in open("demo1.txt").readlines()]

commands = []
for _ in input:
    commands.append([[_[0][0],[[int(_)+100000 for _ in _.split("=")[1].split("..")] for _ in _[1]]]][0])



x = np.zeros(1000000)
y = np.zeros(1000000)
z = np.zeros(1000000)

on = 0

cube = []
zon = 1000000*[]
square = np.zeros((200000,200000))

for command in commands:
    pass

    """
    for z in range(command[1][0][0],command[1][0][1]+1):
        np.zeros((abs(command[1][0][0]-command[1][0][1]),abs(command[1][1][0]-command[1][1][1])))

        if(command[0] == 'on'):
            square[command[1][0][0]:command[1][0][1]+1,command[1][1][0]:command[1][1][1]+1] = 1
        if(command[0] == 'off'):
            pass
    """





#print(np.count_nonzero(cubes))