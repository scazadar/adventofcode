#!/usr/bin/env python3
import numpy as np
f = np.array([[int(x) for x in _] for _ in [x.strip() for x in open("11.txt").readlines()]])
flash_count = 0
x = 0

def add_border(_):
    _ = np.insert(_,0,10*[0],axis=0)
    _ = np.insert(_,len(_),10*[0],axis=0)
    _ = np.insert(_,0,[0],axis=1)
    _ = np.insert(_,len(_[0]),[0],axis=1)
    return _

def remove_border(_):
    _ = np.delete(_,0,axis=0)
    _ = np.delete(_,len(_)-1,axis=0)
    _ = np.delete(_,0,axis=1)
    _ = np.delete(_,len(_[0])-1,axis=1)
    return _

def get_flashs(s,count=0):
    flashed = []
    while(True):  
        s = add_border(s)
        flashs = [_ for _ in list(zip(*np.where(s > 9))) if _ not in flashed]
        s = remove_border(s)
        if(len(flashs) > 0):
            for flash in flashs:
                s = add_border(s)
                s[flash[0]-1][flash[1]-1] += 1
                s[flash[0]-1][flash[1]+1] += 1
                s[flash[0]+1][flash[1]-1] += 1
                s[flash[0]+1][flash[1]+1] += 1
                s[flash[0]][flash[1]+1] += 1
                s[flash[0]][flash[1]-1] += 1
                s[flash[0]-1][flash[1]] += 1
                s[flash[0]+1][flash[1]] += 1
                s[flash[0]][flash[1]] += 1
                count += 1
                s = remove_border(s)
                flashed.append(flash)
        else:
            return [s,count]

while(True):
    f,count = get_flashs(f+1)
    f = np.where(f > 9, 0, f)
    flash_count += count

    if(x == 99):
        print(f"Part1: {flash_count}")
    if(np.all((f == 0))):
        print(f"Part2: {x+1}")
        exit()
    x += 1