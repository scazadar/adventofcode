#!/usr/bin/env python3
f = [x.strip().replace(" ","") for x in open("5.txt").readlines()]
start = [x[0].split(",") for x in [_.split("->") for _ in f]]
end = [x[1].split(",") for x in [_.split("->") for _ in f]]
pmap = dict()
for x in range(len(start)):
    n_x = [int(start[x][0]),int(end[x][0])]
    n_y = [int(start[x][1]),int(end[x][1])]
    if(start[x][0] == end[x][0]):
        n_y.sort()
        for number in [_ for _ in range(n_y[0],n_y[1]+1)]:
            if(f"{start[x][0]},{number}" in pmap.keys()):
                pmap.update({f"{start[x][0]},{number}": pmap.get(f"{start[x][0]},{number}") + 1})
            else:
                pmap.setdefault(f"{start[x][0]},{number}",1)    
    elif(start[x][1] == end[x][1]):
        n_x.sort()
        for number in [_ for _ in range(n_x[0],n_x[1]+1)]:
            if(f"{number},{start[x][1]}" in pmap.keys()):
                pmap.update({f"{number},{start[x][1]}": pmap.get(f"{number},{start[x][1]}") + 1})
            else:
                pmap.setdefault(f"{number},{start[x][1]}",1)
print(len([_ for _ in pmap.values() if _ > 1]))