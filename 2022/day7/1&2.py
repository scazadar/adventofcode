#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
f = [_.strip().split() for _ in open("inputs/day7").readlines()]

current_dir = []
dirs = {}

for _ in f:
    if(len(_) == 2 and "ls" != _[1] and "dir" != _[0]):
        for x in range(len(current_dir)):
            dirs["/".join(current_dir[:x+1])] = dirs["/".join(current_dir[:x+1])] + int(_[0])
    if("$" in _):
        if("cd" == _[1] and "/" == _[2]):
            current_dir = ["/"]
        elif("cd" == _[1] and ".." == _[2]):
            current_dir.pop()
        elif("cd" == _[1]):
            current_dir.append(_[2])
        if(not dirs.get("/".join(current_dir))):
            dirs.setdefault("/".join(current_dir),0)

part1 = []
part2 = []
for _ in dirs:
    if(dirs[_] < 100000):
        part1.append(dirs[_])
    if(70000000 - dirs["/"] + dirs[_]) >= 30000000:
        part2.append(dirs[_])

print("Part1: ",sum(part1))
print("Part2: ",sorted(part2)[0])

 
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s
