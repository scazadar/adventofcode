#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
input = [[_.strip().split()[0],int(_.strip().split()[1])] for _ in open("inputs/day9").readlines()]

visited = []
visited2 = []
head_position = [0,0]
tail_positions = [[0,0] for _ in range(9)]

def move_tail(head_position,tail_position):
    #rechts hoch
    if(head_position[0]-1 > tail_position[0] and head_position[1]-1 > tail_position[1]):
        tail_position[0] += 1
        tail_position[1] += 1
    #rechts runter
    elif(head_position[0]-1 > tail_position[0] and head_position[1]+1 < tail_position[1]):
        tail_position[0] += 1
        tail_position[1] -= 1
    #links hoch
    elif(head_position[0]+1 < tail_position[0] and head_position[1]-1 > tail_position[1]):
        tail_position[0] -= 1
        tail_position[1] += 1
    #links runter
    elif(head_position[0]+1 < tail_position[0] and head_position[1]+1 < tail_position[1]):
        tail_position[0] -= 1
        tail_position[1] -= 1
    #nach rechts
    elif(head_position[0]-1 > tail_position[0]):
        tail_position[0] += 1
        tail_position[1] = head_position[1]
    #nach links
    elif(head_position[0]+1 < tail_position[0]):
        tail_position[0] -= 1
        tail_position[1] = head_position[1]
    #nach oben
    elif(head_position[1]-1 > tail_position[1]):
        tail_position[1] += 1
        tail_position[0] = head_position[0]
    #nach unten
    elif(head_position[1]+1 < tail_position[1]):
        tail_position[1] -= 1
        tail_position[0] = head_position[0]
    return tail_position

for headmove in input:
    for _ in range(headmove[1]):
        if("R" == headmove[0]):
            head_position[0] += 1
        elif("L" == headmove[0]):
            head_position[0] -= 1
        elif("U" == headmove[0]):
            head_position[1] += 1
        elif("D" == headmove[0]):
            head_position[1] -= 1
        
        #Part1
        tail_positions[0] = move_tail(head_position,tail_positions[0])
        visited.append(",".join(map(str,tail_positions[0])))
        #Part2
        for _ in range(len(tail_positions)-1):
            tail_positions[_+1] = move_tail(tail_positions[_],tail_positions[_+1])
        visited2.append(",".join(map(str,tail_positions[-1])))

print("Part 1: ", len(set(visited)))
print("Part 2: ", len(set(visited2)))

    
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.081s
