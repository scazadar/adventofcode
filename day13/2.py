#!/usr/bin/env python3
import numpy as np

np.set_printoptions(linewidth=200)

def hfold(index,paper):
    paper = np.delete(paper,index,0)
    side_1 = paper[:index]
    side_2 = np.flipud(paper[index:len(paper)])

    return merge_side(side_1,side_2)

def vfold(index,paper):
    paper = np.delete(paper,index,1)
    side_1, side_2 = np.split(paper,2,1)
    side_2 = np.fliplr(side_2)

    return merge_side(side_1,side_2)

def merge_side(side_1, side_2):
    for y in range(len(side_2)):
        for x in range(len(side_2[y])):
            if(side_2[y][x] == '█'):
                side_1[y][x] = side_2[y][x]
    return side_1

f = np.array([x.strip() for x in open("13.txt").readlines()])

coordinates, instructions = np.split(f,np.where(f == '')[0])
coordinates = np.array([[int(x) for x in _.split(',')] for _ in coordinates])
instructions = [x.split('=') for x in [_.split(' ')[-1] for _ in np.delete(instructions,0)]]
#paper = np.full((max([_[1] for _ in coordinates])+1,max([_[0] for _ in coordinates])+1), fill_value=('░'))
paper = np.full((int(instructions[1][1])*2+1,int(instructions[0][1])*2+1), fill_value=('░'))

for _ in coordinates:
    paper[_[1]][_[0]] = '█'

for x in range(len(instructions)):
    if(instructions[x][0] == 'y'):
        paper = hfold(int(instructions[x][1]),paper)
    elif(instructions[x][0] == 'x'):
        paper = vfold(int(instructions[x][1]),paper)

output = ["".join(_) for _ in paper]

for _ in output:
    print(_)