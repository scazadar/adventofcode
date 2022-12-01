#!/usr/bin/env python3
import numpy as np
fishs = np.array([int(_) for _ in [x.strip().replace(" ","") for x in open("demo.txt").readlines()][0].split(",")])
for day in range(80): 
    zeros = np.where(fishs == 0)[0]
    if(len(zeros) > 0):
        fishs = np.append(fishs,[9]*len(zeros))
        np.put(fishs,zeros,7)
    fishs = fishs - 1
print(len(fishs))   