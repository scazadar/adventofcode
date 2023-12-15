#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
file = [_ for _ in open("2023/inputs/day13").read().split("\n")]
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
althMirrors = []
altvMirrors = []

def findMirror(i,p):
    if(len(p[:i]) < len(p[i:])):
        u = p[:i]
        d = p[i:i+len(p[:i])]
    elif(len(p[:i]) > len(p[i:])):
        u = p[i-len(p[i:]):i]
        d = p[i:]
    d.reverse()
    matches = 0
    mismatches = 0
    for x,_ in enumerate(u):
        if(_ == d[x]):
            matches += 1
        
        for i,s in enumerate(_):
            if(s != d[x][i]):
                mismatches += 1
        
    return [len(u),matches,mismatches]
        
for p in patterns:
    for y in range(1,len(p)):
        lines = len(p[:y])
        m = findMirror(y,p)
        if(m[0]==m[1]):
            hMirrors.append(lines)
        if(m[0]==m[1]+1 and m[2] == 1):
            althMirrors.append(lines)
  
    hRows = []
    for x,_ in enumerate(p[0]):
        hRows.append([_[x] for _ in p])
    hRows = ["".join(_) for _ in hRows]
    
    for x in range(1,len(hRows)):
        lines = len(hRows[:x])  
        m = findMirror(x,hRows)
        if(m[0]==m[1]):
            vMirrors.append(lines)
        if(m[0]==m[1]+1 and m[2] == 1):
            altvMirrors.append(lines)

        

    
print(f"Part1: {sum(vMirrors) + (sum(hMirrors)*100)}")
print(f"Part2: {sum(altvMirrors) + (sum(althMirrors)*100)}")
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))