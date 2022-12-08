#!/usr/bin/env python3
#Imports
import time
import numpy as np

#Zeit Start
start = time.time()

#Main

def check_high(treehouse,trees):
    visible_trees = 1
    for tree in list(trees)[:-1]:
        if(treehouse <= tree):
            break
        visible_trees += 1
    return visible_trees

forest = np.array([[int(_) for _ in _.strip()] for _ in open("inputs/day8").readlines()])
visible_trees = 0
scenic_scores = []

for row in range(1,len(forest)-1):
    for column in range(1,len(forest[0])-1):
        if(not np.any(forest[row][column] <= forest[row][:column]) or not np.any(forest[row][column] <= forest[row][column+1:]) or not np.any(forest[row][column] <= forest[:,column][:row]) or not np.any(forest[row][column] <= forest[:,column][row+1:])):
            visible_trees += 1      
        visible_trees2 = []
        visible_trees2.append(check_high(forest[row][column], reversed(forest[row][:column])))
        visible_trees2.append(check_high(forest[row][column], forest[row][column+1:]))
        visible_trees2.append(check_high(forest[row][column], reversed(forest[:,column][:row])))
        visible_trees2.append(check_high(forest[row][column], forest[:,column][row+1:]))
        scenic_scores.append(np.prod(visible_trees2))

print("Part 1: ",visible_trees + len(forest) * 2 + len(forest[0])*2 - 4)
print("Part 2: ",max(scenic_scores))
    
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.290s
