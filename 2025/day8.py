#!/usr/bin/env python3
#Imports
import time, math 
from functools import cache

#Zeit Start
start = time.time()

#Main
boxes = [tuple(map(int,n.strip().split(","))) for n in open("inputs/day8").readlines()]

distances = {}
for y,box1 in enumerate(boxes):
    for box2 in boxes[y:]:
        distance = math.sqrt((box2[0]-box1[0])**2 + (box2[1]-box1[1])**2 + (box2[2]-box1[2])**2)
        if(distance > 0):
            distances.setdefault(distance,(box1,box2))
distances = dict(sorted(distances.items()))
closest = [distances[key] for key in distances]

# Alles Schnickschnack für die Katz nachdem es in Part2 klick gemacht hat
""" class JunctionBox():
    def __init__(self,coordinates):  
        self.connections = set()
        self.coordinates = coordinates
         
    def addConnection(self,jb):
        self.connections.update(jb.getAllConnections(set([self])))
        
    def getAllConnections(self, connections = set()):
        connections.add(self)
        for c in self.connections:
            if(not c in connections):  
                connections.update(c.getAllConnections(connections))
        return connections

boxes = [JunctionBox(tuple(map(int,n.strip().split(",")))) for n in open("inputs/day8.sample").readlines()]

distances = {}
for y,box1 in enumerate(boxes):
    for box2 in boxes[y:]:
        distance = math.sqrt((box2.coordinates[0]-box1.coordinates[0])**2 + (box2.coordinates[1]-box1.coordinates[1])**2 + (box2.coordinates[2]-box1.coordinates[2])**2)
        if(distance > 0):
            distances.setdefault(distance,(box1,box2))
distances = dict(sorted(distances.items()))
closest = [distances[key] for key in distances]

for i in range(10):
    jb = closest[i]
    jb[0].addConnection(jb[1])
    jb[1].addConnection(jb[0])
    
groups = []
for box in boxes:
    for g in groups:
        if(g & box.connections):
            g.update(box.connections)
            break
    else:
        groups.append(box.connections)
    
print(f"Part 1: {math.prod(sorted([len(_) for _ in groups],reverse=True)[:3])}") """

# Nicht optimiert aber läuft in 3s durch
groups = []
for x,c in enumerate(closest):
    for g in groups:
        if(g & set([_ for _ in c])):
            g.update(set([_ for _ in c]))
            break                  
    else:
        groups.append(set([_ for _ in c])) 
    reduced = []

    for i,g in enumerate(groups):
        for _ in groups[i+1:]:
            if(_ & g):
                g.update(_)
                reduced.append(_)
                break

    for r in reduced:
        groups.remove(r)
    
    if(x == 9 or x == 999):
        print(f"Part 1: {math.prod(sorted([len(_) for _ in groups],reverse=True)[:3])}")
    
    if(len(groups[0]) == len(boxes)):
        print(f"Part 2: {math.prod([int(_[0]) for _ in c])}")
        break
        


            
    
    




    

    
    



     
        

        


#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))