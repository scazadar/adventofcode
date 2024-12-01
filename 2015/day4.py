#!/usr/bin/env python3
#Imports
import time,hashlib

#Zeit Start
start = time.time()
#Main
key = open("2015/inputs/day4").read()

i = 0
p1 = []
p2 = []
while True:
    hash = hashlib.md5(f"{key}{i}".encode("utf-8")).hexdigest()
    if(str(hash).startswith("00000")):
        p1.append(i)
    if(str(hash).startswith("000000")):
        p2.append(i)
        break
    i += 1

print(f"Part1: {min(p1)}")
print(f"Part2: {min(p2)}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s