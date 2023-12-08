#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
file = open("2023/inputs/day8").read().split("\n")
instruction = file[0]
nodes = {node.split("=")[0].strip():node.split("=")[1].strip("() ").split(", ") for node in file[2:]}

""" currentNode = nodes.get('AAA')
steps = 0
finish = False
while not finish:
    for i in instruction:
        steps += 1
        if(currentNode[0 if i == 'L' else 1] == "ZZZ"):
            finish = True
            break
        currentNode = nodes.get(currentNode[0 if i == 'L' else 1])

print(f"Part1: {steps}") """


currentNodes = [nodes.get(node) for node in nodes if node[2] == "A"]
nextNodes = []
steps = 0
finishCount = 0
print(currentNodes)
while finishCount != len(currentNodes):
    for i in instruction:
        steps += 1
        for currentNode in currentNodes:
            if(currentNode[0 if i == 'L' else 1][2] == "Z"):
                finishCount += 1 
            if(finishCount == len(currentNodes)):
                break
            nextNodes.append(nodes.get(currentNode[0 if i == 'L' else 1]))
        if(len(currentNodes) == len(nextNodes)):
            currentNodes = nextNodes
        else:
            break
        nextNodes = []
        finishCount = 0

print(currentNodes)
print(f"Part2: {steps}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))