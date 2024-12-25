#!/usr/bin/env python3
# Imports
import time

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day25"

locksAndKeys = [_.split("\n") for _ in open(file).read().split("\n\n")]
locks = [[_.index('.') -1 for _ in zip(*[tuple(_ for _ in _) for _ in _])] for _ in locksAndKeys if _[0] == '#####']
keys = [[len(_) - _.index('#') -1 for _ in zip(*[tuple(_ for _ in _) for _ in _])] for _ in locksAndKeys if _[0] != '#####']

print(f"Part1: {sum([1 for lock in locks for key in keys if not any(x >= 6 for x in [l+k for l,k in zip(lock,key)])])}")
            

# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))

