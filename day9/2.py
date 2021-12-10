#!/usr/bin/env python3
from itertools import chain
f = [list(map(int,_)) for _ in [x.strip() for x in open("9.txt").readlines()]]

def basin_bot(y,x):
    Y_SIZE = len(f)
    X_SIZE = len(f[y])
    basin_coordinates = set()

    def basin_bot_x(y,x):
        basin_coordinates.update([f"{y},{x}"])
        for xs in range(x-1,-1,-1):
            if(f[y][xs] != 9 and not set([f"{y},{xs}"]).issubset(basin_coordinates)):
                basin_bot_y(y,xs)
            else:
                break
        for xe in range(x+1,X_SIZE):
            if(f[y][xe] != 9 and not set([f"{y},{xe}"]).issubset(basin_coordinates)):
                basin_bot_y(y,xe)
            else:
                break
    def basin_bot_y(y,x): 
        basin_coordinates.update([f"{y},{x}"]) 
        for ys in range(y-1,-1,-1):
            if(f[ys][x] != 9 and not set([f"{ys},{x}"]).issubset(basin_coordinates)):
                basin_bot_x(ys,x)
            else:
                break
        for ye in range(y+1,Y_SIZE):
            if(f[ye][x] != 9 and not set([f"{ye},{x}"]).issubset(basin_coordinates)):
                basin_bot_x(ye,x)
            else:
                break

    basin_bot_x(y,x)
    return(basin_coordinates)     

basins = []
for y in range(len(f)):
    for x in range(len(f[y])):
        #corners
        if(x == 0 and y == 0):
            if(f[y][x] < f[y][x+1] and f[y][x] < f[y+1][x]):
                basins.append(basin_bot(y,x))
        elif(x == len(f[y])-1 and y == 0):
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y+1][x]):
                basins.append(basin_bot(y,x))
        elif(x == 0 and y == len(f)-1):
            if(f[y][x] < f[y][x+1] and f[y][x] < f[y-1][x]):
                basins.append(basin_bot(y,x))
        elif(x == len(f[y])-1 and y == len(f)-1):
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y-1][x]):
                basins.append(basin_bot(y,x))
        #sides
        elif(x == 0):
            if(f[y][x] < f[y][x+1] and f[y][x] < f[y+1][x] and f[y][x] < f[y-1][x]):
                basins.append(basin_bot(y,x))
        elif(x == len(f[y])-1):
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y+1][x] and f[y][x] < f[y-1][x]):
                basins.append(basin_bot(y,x))
        elif(y == 0):
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y+1][x] and f[y][x] < f[y][x+1]):
                basins.append(basin_bot(y,x))
        elif(y == len(f)-1):
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y-1][x] and f[y][x] < f[y][x+1]):
                basins.append(basin_bot(y,x))
        #other
        else:
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y+1][x] and f[y][x] < f[y-1][x] and f[y][x] < f[y][x+1]):
                basins.append(basin_bot(y,x))

basins_len = []
for basin in basins:
    basins_len.append(len(basin))
    basins_len.sort()
print(basins_len[-1]*basins_len[-2]*basins_len[-3])

##Grafik xD
biggest_basins = []
basins_v = []
for basin in basins:
    if(len(basin) >= basins_len[-3]):
        biggest_basins.append([_ for _ in basin])
    else:
        basins_v.append([_ for _ in basin])

file = [_.strip() for _ in open("9.txt").readlines()]
for _ in range(len(file)):
    for x in range(len(file[_])):
        if(f"{_},{x}" in list(chain(*biggest_basins))):
            print("█", end="")
        elif(f"{_},{x}" in list(chain(*basins_v))):
            print("░", end="")
        else:
            print("▒", end="")
    print()