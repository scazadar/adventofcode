#!/usr/bin/env python3
f = [list(map(int,_)) for _ in [x.strip() for x in open("9.txt").readlines()]]
#corners
summe = 0
for y in range(len(f)):
    for x in range(len(f[y])):
        #corners
        if(x == 0 and y == 0):
            if(f[y][x] < f[y][x+1] and f[y][x] < f[y+1][x]):
                summe += f[y][x] +1
        elif(x == len(f[y])-1 and y == 0):
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y+1][x]):
                summe += f[y][x] + 1
        elif(x == 0 and y == len(f)-1):
            if(f[y][x] < f[y][x+1] and f[y][x] < f[y-1][x]):
                summe += f[y][x] +1
        elif(x == len(f[y])-1 and y == len(f)-1):
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y-1][x]):
                summe += f[y][x] +1
        #sides
        elif(x == 0):
            if(f[y][x] < f[y][x+1] and f[y][x] < f[y+1][x] and f[y][x] < f[y-1][x]):
                summe += f[y][x] +1
        elif(x == len(f[y])-1):
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y+1][x] and f[y][x] < f[y-1][x]):
                summe += f[y][x] +1
        elif(y == 0):
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y+1][x] and f[y][x] < f[y][x+1]):
                summe += f[y][x] +1
        elif(y == len(f)-1):
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y-1][x] and f[y][x] < f[y][x+1]):
                summe += f[y][x] +1
        #other
        else:
            if(f[y][x] < f[y][x-1] and f[y][x] < f[y+1][x] and f[y][x] < f[y-1][x] and f[y][x] < f[y][x+1]):
                summe += f[y][x] +1

print(summe)