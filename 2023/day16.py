#!/usr/bin/env python3
#Imports
import time
from collections import deque

#Zeit Start
start = time.time()

#Main
rows = open("2023/inputs/day16").read().split("\n")

def process(cursors):
    usedSplitter = []
    energized = set()
    while len(cursors) > 0:
        newCursors = deque([])
        for cursor in cursors:
            if(cursor[2] == "r"):
                nextPosition = (cursor[0]+1,cursor[1],"r")
            elif(cursor[2] == "l"):
                nextPosition = (cursor[0]-1,cursor[1],"l")
            elif(cursor[2] == "u"):
                nextPosition = (cursor[0],cursor[1]-1,"u")
            elif(cursor[2] == "d"):
                nextPosition = (cursor[0],cursor[1]+1,"d")

            if(not nextPosition[:2] in usedSplitter and nextPosition[0] >= 0 and nextPosition[1] >= 0 and nextPosition[0] < len(rows[0]) and nextPosition[1] < len(rows)):
                energized.add(f"{nextPosition[:2]}")
                if(rows[nextPosition[1]][nextPosition[0]] == "|" and (cursor[2] == "r" or cursor[2] == "l")):
                    newCursors.append((*nextPosition[:2],"u"))
                    newCursors.append((*nextPosition[:2],"d"))
                    usedSplitter.append(nextPosition[:2])
                elif(rows[nextPosition[1]][nextPosition[0]] == "-" and (cursor[2] == "u" or cursor[2] == "d")):
                    newCursors.append((*nextPosition[:2],"l"))
                    newCursors.append((*nextPosition[:2],"r"))
                    usedSplitter.append(nextPosition[:2])
                elif(rows[nextPosition[1]][nextPosition[0]] == "/"):
                    if(cursor[2] == "l"):
                        newCursors.append((*nextPosition[:2],"d"))
                    elif(cursor[2] == "d"):
                        newCursors.append((*nextPosition[:2],"l"))   
                    elif(cursor[2] == "r"):
                        newCursors.append((*nextPosition[:2],"u"))
                    elif(cursor[2] == "u"):
                        newCursors.append((*nextPosition[:2],"r"))   
                elif(rows[nextPosition[1]][nextPosition[0]] == "\\"):
                    if(cursor[2] == "l"):
                        newCursors.append((*nextPosition[:2],"u"))
                    elif(cursor[2] == "u"):
                        newCursors.append((*nextPosition[:2],"l"))   
                    elif(cursor[2] == "r"):
                        newCursors.append((*nextPosition[:2],"d"))
                    elif(cursor[2] == "d"):
                        newCursors.append((*nextPosition[:2],"r")) 
                else:
                    newCursors.append(nextPosition)

        cursors = newCursors
    return energized


print(f'Part1: {len(process([[-1,0,"r"]]))}')

configs = []
for _ in range(len(rows)):
    configs.append(len(process([[-1,_,"r"]])))
    configs.append(len(process([[len(rows[_]),_,"l"]])))

for _ in range(len(rows[0])):
    configs.append(len(process([[_,-1,"d"]])))
    configs.append(len(process([[_,len(rows),"u"]])))

print(f'Part2: {max(configs)}') 

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))