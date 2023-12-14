#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
file = [_ for _ in open("2023/inputs/day13.sample").read().split("\n")]
file.append("")

patterns = []
pattern = []
for _ in file:
    if(_ == ""):
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(_)

hMirrors = []
vMirrors = []
#althMirrors = []
#altvMirrors = []

def findMirror(i,p):
    if(len(p[:i]) < len(p[i:])):
        u = p[:i]
        d = p[i:i+len(p[:i])]
    elif(len(p[:i]) > len(p[i:])):
        u = p[i-len(p[i:]):i]
        d = p[i:]
    d.reverse()
    return u == d
        
for p in patterns:
    for y in range(1,len(p)):
        lines = len(p[:y])
        if(findMirror(y,p)):
            hMirrors.append(lines)
  
    hRows = []
    for x,_ in enumerate(p[0]):
        hRows.append([_[x] for _ in p])
    hRows = ["".join(_) for _ in hRows]
    
    for x in range(1,len(hRows)):
        lines = len(hRows[:x])  
        if(findMirror(x,hRows)):
            vMirrors.append(lines)

        

    
print(f"Part1: {sum(vMirrors) + (sum(hMirrors)*100)}")
#print(f"Part2: {sum(altvMirrors) + (sum(althMirrors)*100)}")
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))