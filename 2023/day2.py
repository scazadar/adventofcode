#!/usr/bin/env python3
#Imports
import time, math

#Zeit Start
start = time.time()

#Main
idsum = 0
powersum = 0
for s in open("2023/inputs/day2").read().split("\n"):
    id = int(s.split(':')[0].split()[1])
    sets = [{e.strip().split(' ')[1]:int(e.strip().split(' ')[0]) for e in set.split(',')} for set in s.split(':')[1].split(";")]

    gamepossible = True
    blue = []
    red = []
    green = []
    for s in sets:
        blue.append(s.get('blue',0))
        red.append(s.get('red',0))
        green.append(s.get('green',0))
        
        if(s.get('blue',0) > 14 or s.get('red',0) > 12 or s.get('green',0) > 13):
            gamepossible = False
    power = math.prod([max(blue),max(red),max(green)])
    powersum += power
    if(gamepossible):
        idsum += id
        
print('Part1: ', idsum)
print('Part2: ', powersum)
        
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s