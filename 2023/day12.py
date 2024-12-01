#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
lines = [[_.split(" ")[0],[int(_) for _ in _.split(" ")[1].split(",")]] for _ in open("2023/inputs/day12.sample").read().split("\n")]

def splitSprings(group):
    return [len(_) for _ in group.split(".") if _ != '']
    
arrangements = 0

for _ in lines:
    print("----------x")
    print(_[1])
    qi = []
    for x,c in enumerate(_[0]):
        if c == '?':
            qi.append(x)
    print(f"qi: {len(qi)}")

    arrangement = 0
    for i in range(2 ** len(qi)):
        v = format(i,'b').zfill(len(qi)).replace("1","#").replace("0",".")
        s = ""
        for x,c in enumerate(_[0]):
            if(x in qi):
                s += v[qi.index(x)]
            else:
                s += c
                    
        if(splitSprings(s) == _[1]):
            arrangement += 1
           
    print(arrangement)
    
    qi2 = []
    _[0] = f"{_[0]}"
    for x,c in enumerate(_[0]):
        if c == '?':
            qi2.append(x)
    print(f"qi2: {len(qi2)}")

    arrangement2 = 0
    for i in range(2 ** len(qi2)):
        v = format(i,'b').zfill(len(qi2)).replace("1","#").replace("0",".")
        s = ""
        for x,c in enumerate(_[0]):
            if(x in qi2):
                s += v[qi2.index(x)]
            else:
                s += c
                    
        if(splitSprings(s) == _[1]):
            arrangement2 += 1
    print(arrangement2)
    
    print(arrangement * (arrangement2**4))
           
    arrangements += arrangement * (arrangement2**4)

print(f"Part1: {arrangements}")
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))