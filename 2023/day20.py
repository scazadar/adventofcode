#!/usr/bin/env python3
#Imports
import time
#Zeit Start
start = time.time()

#Main
f = [[_.split(" -> ")[0],_.split(" -> ")[1].replace(" ","").split(",")] for _ in open("2023/inputs/day20").read().split("\n")]

def initModules():
    modules = {"output":["broadcaster",0,[],[]]}
    for _ in f:
        if(_[0] == "broadcaster"):
            for n in _[1]:
                modules["broadcaster"] = ["broadcaster",0,_[1],[]]
        else:
            #[type,state,nextModules,previousModules]
            modules[_[0][1:]] = [_[0][0],0,_[1],[]]
    for k,m in modules.items():
        for n in m[2]:
            if(n in modules):
                modules[n][3].append(k)
    return modules

def process(module,signal,modules):
    if(modules[module][0] == "broadcaster"):
        modules[module][1] = signal
    elif(modules[module][0] == "%"):
        if(signal == 0):
            modules[module][1] = 1 if modules[module][1] == 0 else 0
    elif(modules[module][0] == "&" ):
        states = []
        for p in modules[module][3]:
            states.append(modules[p][1])
        if(0 in states):
            modules[module][1] = 1
        else:
            modules[module][1] = 0     
    lows = 0
    highs = 0 
    rx = False
    for n in modules[module][2]:
        if(modules[module][1] == 0):
            lows += 1
        elif(modules[module][1] == 1):
            highs += 1
        if(n == "rx" and modules[module][1] == 0):
            rx = True
        if(n in modules):
            if((modules[n][0] == "%" and modules[module][1] == 0) or modules[n][0] == "&" or module == "broadcaster"):
                    processChain.append([n,modules[module][1]])
    return [lows,highs,rx]

modules = initModules()
lows = 0
highs = 0
processChain = []
print(modules["dd"])
for x in range(1000):
    processChain.append(["broadcaster",0])
    lows += 1
    for p in processChain:
        r = process(p[0],p[1],modules)
        lows += r[0]
        highs += r[1]
    processChain = []

print(f"Part1: {lows*highs}")


processChain = []
buttonPressed = 0
modules = initModules()
while True:
    buttonPressed += 1
    processChain.append(["broadcaster",0])
    for p in processChain:
        r = process(p[0],p[1],modules)
    if(r[2]):
        break
    processChain = []
    
print(f"Part2: {buttonPressed}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))