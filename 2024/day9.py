#!/usr/bin/env python3
# Imports
import time
from itertools import combinations

# Zeit Start
start = time.time()

# Main
diskMap = open("2024/inputs/day9").read().strip()

filesystem = []
filesystem2 = []
filesystem2Files = []

id = 0
for i,b in enumerate(diskMap):
    #Part1
    filesystem.extend(("." for _ in range(int(b))) if i % 2 == 1 else (str(id) for _ in range(int(b))))
    #Part2
    filesystem2 = filesystem.copy()
    filesystem2Files.append((".",len(list(str(id) for _ in range(int(b))))) if i % 2 == 1 else (id,len(list(str(id) for _ in range(int(b))))))
    #######
    id += 1 if i % 2 == 0 else 0
    

checksum = 0
for i,b in enumerate(filesystem[::-1]):
    if(b != '.' and set(filesystem[filesystem.index("."):]) != {"."}):
        filesystem[filesystem.index(".")] = b
        filesystem[len(filesystem) - i -1] = "."
    if(filesystem[i] != '.'):
        checksum += i * int(filesystem[i])
print(f"Part1: {checksum}")


checksum = 0
for id,c in reversed(filesystem2Files):
    if(id != '.'):
        indizes = list(filter(lambda i: filesystem2[i] == ".", range(len(filesystem2))))
        for n in indizes:
            if(set(filesystem2[n:n+c]) == {"."}):
                for i in range(c):
                    if(n+i < len(filesystem2)):
                        filesystem2[n+i] = str(id)
                        filesystem2[len(filesystem2) - list(reversed(filesystem2)).index(str(id)) -1 ] = "."
                break
        
for i,n in enumerate(filesystem2):
    checksum += i*int(n) if n != '.' else 0

print(f"Part2: {checksum}")


# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))