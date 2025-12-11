#!/usr/bin/env python3
#Imports
import time, re, sys

#Zeit Start
start = time.time()

#Main

#Part 1
input = [r for r in open("inputs/day11").readlines()]
devices = {_.split(":")[0]:_.split(":")[1].strip().split() for _ in input}

paths = ["you"]
pathCount = 0

while len(paths) > 0:
    tempPaths = paths.copy()
    for path in paths:
        if(path=="out"):
            pathCount += 1
        else:
            tempPaths.extend([nextPath for nextPath in devices[path]])
        tempPaths.remove(path)
    paths = tempPaths
    
print(f"Part 1: {pathCount}")
        
# Part 2
#input = [r for r in open("inputs/day11_2.sample").readlines()]
#devices = {_.split(":")[0]:_.split(":")[1].strip().split() for _ in input}

paths = {_:0 for _ in devices}
dacPaths = paths.copy()
fftPaths = paths.copy()
validPaths = paths.copy()

paths['svr'] += 1
pathCount = 0
end = False

while not end: 
    end = True 
    tempPaths = paths.copy()
    for path in paths:
        for p in devices[path]:
            if(p == "out"):
                break
            elif(p == "dac"):
                dacPaths[p] += paths[path]
            elif(p == "fft"):
                fftPaths[p] += paths[path]
            else:
                tempPaths[p] += paths[path]
        tempPaths[path] -= paths[path]
        if(tempPaths[path] > 0):
            end = False
    paths = tempPaths
    
    tempPaths = dacPaths.copy()
    for path in dacPaths:
        for p in devices[path]:
            if(p == "out"):
                break
            elif(p == "fft"):
                validPaths[p] += dacPaths[path]
            else:
                tempPaths[p] += dacPaths[path]
        tempPaths[path] -= dacPaths[path]
        if(tempPaths[path] > 0):
            end = False
    dacPaths = tempPaths
    
    tempPaths = fftPaths.copy()
    for path in fftPaths:
        for p in devices[path]:
            if(p == "out"):
                break
            elif(p == "dac"):
                validPaths[p] += fftPaths[path]
            else:
                tempPaths[p] += fftPaths[path]
        tempPaths[path] -= fftPaths[path]
        if(tempPaths[path] > 0):
            end = False
    fftPaths = tempPaths
    
    tempPaths = validPaths.copy()
    for path in validPaths:
        for p in devices[path]:
            if(p == "out"):
                pathCount += validPaths[path]
            else:
                tempPaths[p] += validPaths[path]
        tempPaths[path] -= validPaths[path]
        if(tempPaths[path] > 0):
            end = False
    validPaths = tempPaths

print(f"Part 2: {pathCount}")
   
    

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))