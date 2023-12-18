#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
f = [[_.split(" ")[0],int(_.split(" ")[1]),_.split(" ")[2].strip("#()")] for _ in open("2023/inputs/day18").read().split("\n")]

def getEdges(cmds):
    x = 0
    y = 0
    edgeLength = 0
    edges = []
    for cmd in cmds:
        if(cmd[0] == "R"):
            x += cmd[1]
        elif(cmd[0] == "L"):
            x -= cmd[1]
        elif(cmd[0] == "D"):
            y += cmd[1]
        elif(cmd[0] == "U"):
            y -= cmd[1]
        edgeLength += cmd[1]
        edges.append([x,y])
    return [edges,edgeLength]

edges,edgeLength = getEdges(f) 
lagoon = sum([(edges[_][1]+edges[_+1][1])*(edges[_][0]-edges[_+1][0]) for _ in range(len(edges)-1)]) // 2
print(f"Part1: {lagoon + (edgeLength // 2) +1}")

part2cmds = []    
for _ in f:
    d = ""
    if(_[2][-1] == '0'):
        d = "R"
    elif(_[2][-1] == '1'):
        d = "D"
    elif(_[2][-1] == '2'):
        d = "L"
    elif(_[2][-1] == '3'):
        d = "U"

    part2cmds.append([d,int(_[2][:-1],16)])
    
edges,edgeLength = getEdges(part2cmds) 
lagoon = sum([(edges[_][1]+edges[_+1][1])*(edges[_][0]-edges[_+1][0]) for _ in range(len(edges)-1)]) // 2
print(f"Part2: {lagoon + (edgeLength // 2) +1}")

    
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))