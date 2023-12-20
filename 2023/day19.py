#!/usr/bin/env python3
#Imports
import time
import re
import math

#Zeit Start
start = time.time()

#Main
f = open("2023/inputs/day19.sample").read().split("\n")

workflows = {_.split("{")[0]:[_.split(":") for _ in _.split("{")[1].strip("}").split(",")] for _ in f[:f.index('')]}
ratings = [{_.split("=")[0]:int(_.split("=")[1]) for _ in _.strip("{}").split(",")} for _ in f[f.index('')+1:]]

A = []
R = []

def prozess(workflow,rating):
    for w in workflow:
        if(len(w) == 1):
            if(w[0] == "A" or w[0] == "R"):
                return w[0]
            else:
                return prozess(workflows.get(w[0]),rating)
        elif(eval(f"{rating.get(w[0][0])}{w[0][1]}{re.split("[<>]",w[0])[1]}")):
            if(w[1] == "A" or w[1] == "R"):
                return w[1]
            else:
                return prozess(workflows.get(w[1]),rating)

#Part2 noch nicht fertig aber irgendwie in die Richtung

def prozessPart2(workflow,c):
    combinations = 0
    
    print(workflow)
    #[x,m,a,s]
    for w in workflow:
        if(len(w) == 1):
            if(w[0] == "A"):
                combinations += math.prod([c[_] for _ in c])
        else:
            e = re.split("[<>]",w[0])
            i = int(e[1])
            
            if("<" in w[0]):
                range =  [i - 1,c.get(e[0]) - i ]
            else:
                range = [c.get(e[0]) - i - i ,i - 1]
            
            c[w[0][0]] = range

            if(w[1] == "A"):
                combinations += math.prod([c[_] for _ in c])
            else:
                c2 = c
                c2[w[0][0]] = range[0]
                combinations += prozessPart2(workflows.get(w[1]),c2)
        
    return combinations
                

for rating in ratings:
    result = prozess(workflows.get("in"),rating)    
    if(result == "A"):
        A.append(rating)
    elif(result == "R"):
        R.append(rating)

print(f"Part1: {sum([sum([_[k] for k in _]) for _ in A])}")



#[x,m,a,s]
print(prozessPart2(workflows.get("in"),{"x":[0,4000],"m":[0,4000],"a":[0,4000],"s":[0,4000]}))








   
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))