#!/usr/bin/env python3
import numpy as np
f = [_.split("-") for _ in [x.strip() for x in open("12.txt").readlines()]]

connections_1 = [] 
connections_2 = [] 
paths = []

def get_next_connections(s,lower_case_visited):
    next_connections = []
    for x in range(len(connections_1)):
        if(connections_1[x] == s and connections_2[x] != "start" and connections_2[x] not in lower_case_visited):
            next_connections.append(connections_2[x])
        if(connections_2[x] == s and connections_1[x] != "start" and connections_1[x] not in lower_case_visited):
            next_connections.append(connections_1[x])
    return next_connections
        
for _ in f:
    connections_1.append(_[0])
    connections_2.append(_[1])

#Start
for x in range(len(connections_1)):
    if(connections_1[x] == "start"):
        new_path = []
        new_path.append(connections_1[x])
        new_path.append(connections_2[x])
        paths.append(new_path)
for x in range(len(connections_2)):
    if(connections_2[x] == "start"):
        new_path = []
        new_path.append(connections_2[x])
        new_path.append(connections_1[x])
        paths.append(new_path)


finished_paths = []
while(True):
    new_paths = []
    for y in range(len(paths)):
        lower_case_visited = []
        path = paths.pop()
        for _ in path:
            if(_.islower()):
                lower_case_visited.append(_)
        if(path[-1] != "end"):
            for visited_num in lower_case_visited:
                twice = False
                if(np.count_nonzero(np.array(lower_case_visited) == visited_num ) >= 2 and visited_num != "start"):
                    twice = True
                    break
            if(not twice):
                lower_case_visited = []
            next_connections = get_next_connections(path[-1],lower_case_visited)
            for connection in next_connections:
                new_path = path.copy()
                new_path.append(connection)
                new_paths.append(new_path)
        else:
            finished_paths.append(path)
    paths = new_paths

    if(len(paths) == 0):
        break


#print(finished_paths)
print(len(finished_paths))