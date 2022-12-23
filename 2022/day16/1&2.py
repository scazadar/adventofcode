#!/usr/bin/env python3
#Imports
import time
from parse import parse

#Zeit Start
start = time.time()

#Main

f = [_.strip() for _ in open("inputs/day16.sample").readlines()]

valve_opend = []
current_tunnel = "AA"
valves = {}
pressure = 0


for _ in f:
    valve = parse("Valve {} has flow rate={:d}; tunnel leads to valve {}",_)
    if(not valve):
        valve = parse("Valve {} has flow rate={:d}; tunnels lead to valves {}",_)
    valves.setdefault(valve[0],[valve[1],valve[2].split(", ")])

paths = []

def move(minutes,tunnel,pressure,valve_opened,path):
    #print(minutes,tunnel,pressure,valve_opened)
    paths.append(",".join(path))
    for next_tunnel in valves[tunnel][1]:
        new_path = path
        new_path.append(next_tunnel)
        new_pressure = pressure
        new_minutes = minutes
        new_valve_opened = valve_opened
        new_minutes += 1
        
        if(tunnel not in new_valve_opened):
            if(valves[tunnel][0] != 0):
                new_minutes += 1
                new_pressure = new_pressure + ((30-new_minutes)*valves[tunnel][0])
            new_valve_opened.append(tunnel)
        if(new_minutes >= 30):
            print(",".join(new_path))
            print(new_pressure)
            return
        if(",".join(new_path) not in paths and len(valves) > len(valve_opened)):
            new_minutes = move(new_minutes,next_tunnel,new_pressure,new_valve_opened,new_path)


move(0,"AA",0,[],[])

"""
move = False
openvalve = False

for x in range(30):
    print(f"{x+1}: "+current_tunnel)
    move = not move
    print(valves[current_tunnel][0])
    if(not move and valves[current_tunnel][0] == 0):
        move = False


    if(move):
        for tunnel in valves[current_tunnel][1]:
            if(tunnel not in visited):
                current_tunnel = tunnel
                visited.append(current_tunnel)
                break
        else:
            current_tunnel = valves[current_tunnel][1][0]
"""

    






        


#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s