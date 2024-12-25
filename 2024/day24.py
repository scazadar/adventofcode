#!/usr/bin/env python3
# Imports
import time
import functools
import re
import itertools

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day24.sample"

wiresInit,gates = open(file).read().split("\n\n")

wiresInit = {_.split(":")[0]:bool(int(_.split(":")[1].strip())) for _ in wiresInit.split("\n")}
gates = [re.findall(r"\w+",_) for _ in gates.split("\n")]

class Wire:
    def __init__(self):
        self.outputs:list[Gate] = []
        self.state = None
        
    def setState(self,state):
        self.state = state
        for output in self.outputs:
            output.process()

class Gate:    
    def __init__(self,w1,w2,ow,typ):
        self.w1:Wire = w1
        self.w2:Wire = w2
        self.ow:Wire = ow
        self.typ = typ
        
    def process(self):
        if(self.w1.state != None and self.w2.state != None):
            if(self.typ == "AND"):
                self.ow.setState(self.w1.state & self.w2.state)
            elif(self.typ == "OR"):
                self.ow.setState(self.w1.state | self.w2.state)
            elif(self.typ == "XOR"):
                self.ow.setState(self.w1.state ^ self.w2.state)
                
wires = {_2:Wire() for _ in gates for _2 in _ if _2 not in ("OR","AND","XOR")}

#Connect
for gate in gates:
    g = Gate(wires[gate[0]],wires[gate[2]],wires[gate[3]],gate[1])
    wires[gate[0]].outputs.append(g)
    wires[gate[2]].outputs.append(g)

for i in wiresInit:
    wires[i].setState(wiresInit[i])
        
print(f"Part1: {int("".join([str(int(wires[_].state)) for _ in sorted([_ for _ in wires if _.startswith("z")], reverse=True)]),2)}")
    
#Part 2

def validate(wires:Wire):
    xWires = "".join([str(int(wires[_].state)) for _ in sorted([_ for _ in wires if _.startswith("x")], reverse=True)])
    yWires = "".join([str(int(wires[_].state)) for _ in sorted([_ for _ in wires if _.startswith("y")], reverse=True)])
    zWires = "".join([str(int(wires[_].state)) for _ in sorted([_ for _ in wires if _.startswith("z")], reverse=True)])

    return int(xWires,2) & int(yWires,2) == int(zWires,2)

def getDiffs(original, permutation):
    return [o for o, p in zip(original, permutation) if o != p]

allGateOutputs = [_[3] for _ in gates]
allPermutations = tuple(_ for _ in itertools.permutations(allGateOutputs) if len(getDiffs(allGateOutputs,_)) == 4)

for permutation in allPermutations:
    wires = {_2:Wire() for _ in gates for _2 in _ if _2 not in ("OR","AND","XOR")}
    for i,gate in enumerate(gates):
        g = Gate(wires[gate[0]],wires[gate[2]],wires[permutation[i]],gate[1])
        wires[gate[0]].outputs.append(g)
        wires[gate[2]].outputs.append(g)
        
    for i in wiresInit:
        wires[i].setState(wiresInit[i])

    if(validate(wires)):
        print(f"Part2: {",".join(sorted(getDiffs(allGateOutputs,permutation)))}")
        break

# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))

