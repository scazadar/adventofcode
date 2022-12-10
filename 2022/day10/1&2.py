#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
input = [_.strip().split() for _ in open("inputs/day10").readlines()]

cycles = 0
x = 1
signal_strengths = []
display = [['.' for _ in range (40)] for _ in range(6)]

def display_output():
    display[int(cycles/40)][cycles-(int((cycles/40))*40)] = "█" if cycles-(int((cycles/40))*40) in [x-1,x,x+1] else '░'

for cmd in input:
    if(cmd[0] == "noop"):
        display_output()
        cycles += 1
    else:
        for _ in range(2):
            display_output()
            cycles += 1
            if(cycles in [20,60,100,140,180,220]):
                signal_strengths.append(cycles*x)
        x += int(cmd[1])
        
print("Part1: ",sum(signal_strengths))
print("Part2: ")
for row in display:
    print(''.join(row),'\n',end="")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s

