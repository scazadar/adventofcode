#!/usr/bin/env python3
# Imports
import time
import functools

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day21.sample"

cmds = [[_ for _ in _.strip()] for _ in open(file).readlines()]

numericKeypad = (('7','8','9'),('4','5','6'),('1','2','3'),('.','0','A'))
directionalKeypad = (('.',(-1,0),'A'),((0,-1),(1,0),(0,1)))

@functools.cache
def getCoordinates(l,value):
    return [(y,_.index(value)) for y,_ in enumerate(l) if value in _][0]

def getPaths(m,start,cmd):
    def getNextCursors(path,m,visitedWithCosts):
        directions = ((0,1),(1,0),(0,-1),(-1,0))
        cursor = path[0][-1]

        newPaths = []
        for d in directions:
            dy, dx = d
            next_y, next_x = cursor[0] + dy, cursor[1] + dx
            costs = path[1]
            dirs = path[2].copy()
            if(0 <= next_y < len(m) and 0 <= next_x < len(m[0]) and m[next_y][next_x] not in ['.'] and (next_y,next_x) not in path[0]):
                costs += 1    
                if((next_y,next_x) not in visitedWithCosts or costs <= visitedWithCosts[(next_y,next_x)]):
                    visitedWithCosts[(next_y,next_x)] = costs
                    dirs.append(d)
                    newPaths.append([path[0] + [(next_y,next_x)],costs,dirs])
        return newPaths,visitedWithCosts
    
    
    nmb = cmd.pop(0)
    end = getCoordinates(m,nmb)
    finished = []
    visitedWithCosts = {}
    paths = [[[start],0,[]]]
    if(start==end):
        #return [[[start],0,[]]]
        return [['A']]
    while True:
        newPaths = []
        for path in paths:
            if(start!=end):
                nextPaths,visitedWithCosts = getNextCursors(path,m,visitedWithCosts)
            else:
                nextPaths = [path[0] + [start], path[1],path[2]]
            for p in nextPaths:
                if(p[0][-1] == end):
                    p[2].append('A')
                    if not cmd:
                        finished.append(p[2])
                    else:
                        for _ in getPaths(m,end,cmd):
                            if(p[2] + _ not in finished):
                                finished.append(p[2] + _)
                        #finished.extend(getPaths(m,end,cmd,p))

                else:
                    newPaths.extend(nextPaths)
        if(len(newPaths) == 0):
            break
        paths = newPaths
    return finished

sequences = []

for cmd in cmds:
    start = getCoordinates(numericKeypad,'A')
    #sequence=[]
    #for nmb in cmd:
    #end = getCoordinates(numericKeypad,nmb)
    print(cmd)
    paths = getPaths(numericKeypad,start,cmd)[0]

    for x in range(2):
        start = getCoordinates(directionalKeypad,'A')
        paths = getPaths(directionalKeypad,start,paths)[0]
        print(paths)
    
    #print(paths)
    #break
"""    paths2 = []
    for path in paths:
        #print(path)
        paths2 = getPaths(directionalKeypad,start,[_[2] for _ in path])
        
    print(paths2)
    
    
    break
    path[0][2].append('A')
    sequence.extend([_[2] for _ in path])
    if(path):
        start = path[0][0][-1]
    
    
    for x in range(2):
        start = getCoordinates(directionalKeypad,'A')
        nextSequence = [_2 for _ in sequence for _2 in _]
        sequence=[]
        for d in nextSequence:
            end = getCoordinates(directionalKeypad,d)
            path = getPaths(directionalKeypad,start,end)
            path[0][2].append('A')
            sequence.extend([_[2] for _ in path])
            if(path):
                start = path[0][0][-1] 
        
    sequence = [_2 for _ in sequence for _2 in _]
    
    sequences.append(sequence) """

for s in sequences:
    print(s)
# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))


"""
029A: <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
980A: <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A


<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
v<<A>>^A<A>AvA<^AA>A<vAAA>^A
<A^A>^^AvvvA
029A


+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
    
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""