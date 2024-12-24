#!/usr/bin/env python3
# Imports
import time
import re
import functools

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day23"
connections = tuple(
    tuple(sorted(re.findall(r'[\w]+', _))) for _ in open(file).readlines())

def getAllConnections(mConnections, connections):
    allConnections = set()
    for connection in connections:
        c1 = set()
        c2 = set()

        for computers in [_ for _ in mConnections if connection[0] in _]:
            com = list(computers)
            com.remove(connection[0])
            c1.add(tuple(com))
        for computers in [_ for _ in mConnections if connection[1] in _]:
            com = list(computers)
            com.remove(connection[1])
            c2.add(tuple(com))

        for com in list(c1 & c2):
            allConnections.add(tuple(sorted([*connection, *com])))
    return allConnections

tCount = 0
for _ in getAllConnections(connections, connections):
    for com in _:
        if (com.startswith('t')):
            tCount += 1
            break

print(f"Part1: {tCount}")

# Part2
ac = connections
allConnections = set()

while ac:
    allConnections = ac
    ac = getAllConnections(ac, connections)

print(f"Part2: {",".join(sorted(list(allConnections)[0]))}")

# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))
