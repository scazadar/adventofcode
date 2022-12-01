#!/usr/bin/env python3
f = [x.strip() for x in open("3.txt").readlines()]
o = f
c = f
for b in range(12):
    if(len(o) > 1):
        q = [y for y in o if y[b] == "1"]
        w = [y for y in o if y[b] == "0"]
        o = q if len(q) >= len(w) else w
    if(len(c) > 1):
        q = [y for y in c if y[b] == "1"]
        w = [y for y in c if y[b] == "0"]
        c = w if len(w) <= len(q) else q
print(int(o[0],2)*int(c[0],2))