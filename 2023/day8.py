#!/usr/bin/env python3
#Imports
import time
import math

#Zeit Start
start = time.time()

#Main
file = open("2023/inputs/day8").read().split("\n")
instruction = file[0]
nodes = {node.split("=")[0].strip():node.split("=")[1].strip("() ").split(", ") for node in file[2:]}

currentNode = nodes.get('AAA')
steps = 0
finish = False
while not finish:
    for i in instruction:
        steps += 1
        if(currentNode[0 if i == 'L' else 1] == "ZZZ"):
            finish = True
            break
        currentNode = nodes.get(currentNode[0 if i == 'L' else 1])

print(f"Part1: {steps}") 

<<<<<<< HEAD

currentNodes = [node for node in nodes if node[2] == "A"]
nextNodes = []
steps = 0
finishCount = 0
print(currentNodes)




for node in currentNodes:
    steps = 0
    finish = False
    currentNode = nodes.get(node)
    while not finish:
        for i in instruction:
            steps += 1
            if(currentNode[0 if i == 'L' else 1][2] == "Z"):
                finish = True
                if(currentNode[0 if i == 'L' else 1] not in currentNodes):
                    currentNodes.append(currentNode[0 if i == 'L' else 1])
=======
currentNodes = [[node,0] for node in nodes if node[2] == "A"]
for x,node in enumerate(currentNodes):
    finish = False
    currentNode = nodes.get(node[0])
    while not finish:
        for i in instruction:
            node[1] += 1
            if(currentNode[0 if i == 'L' else 1][2] == "Z"):
                finish = True
                if(currentNode[0 if i == 'L' else 1] not in [n[0] for n in currentNodes]):
                    currentNodes.append([currentNode[0 if i == 'L' else 1],0])
>>>>>>> 162f17eb3cdc2ec9b28c23eab405e9372b88caf0
                break
            else:
                currentNode = nodes.get(currentNode[0 if i == 'L' else 1])

print(f"Part2: {math.lcm(*[node[1] for node in currentNodes])}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))