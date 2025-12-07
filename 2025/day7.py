#!/usr/bin/env python3
#Imports
import time, math

#Zeit Start
start = time.time()

#Main
diagram = [n.strip() for n in open("inputs/day7").readlines()]
   
beams = [_ if _ == '.' else '|' for _ in diagram[0] ]

splitted = 0
for row in diagram[1:]:
    for x,c in enumerate(row):
        if(c == "^" and beams[x] == '|'):
            splitted += 1
            beams[x] = '.'
            beams[x-1] = '|'
            beams[x+1] = '|'
            
print(f"Part 1: {splitted}")

beams = [_ if _ == '.' else '|' for _ in diagram[0] ]
timelines = {x:0 for x,_ in enumerate(beams) }
timelines[beams.index('|')] += 1 

for row in diagram[1:]:
    tempTimelines = timelines.copy()
    for x,c in enumerate(row):
        if(c == "^" and timelines[x] > 0):
            tempTimelines[x-1] += timelines[x]
            tempTimelines[x+1] += timelines[x]
            tempTimelines[x] = 0
    timelines = tempTimelines
        
print(f"Part 2: {sum([timelines[k] for k in timelines])}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))