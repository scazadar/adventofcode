#!/usr/bin/env python3
import numpy as np
input = [[int(_) for _ in x.strip().replace("#","1").replace(".","0")] for x in open("20.txt").readlines()]

IEA = input[0]
input = np.array([[_ for _ in _] for _ in input[2:]])
input = np.pad(input,3)

part1 = 0
for _ in range(50):
    resized_image = np.pad(input,2, mode='constant', constant_values=input[0,0])
    new_image = np.full([len(resized_image[0]),len(resized_image)], 0)

    for x in range(0,len(new_image[0]-2)):
        for y in range(0,len(new_image)-2):
            sub_image_value = resized_image[x:x+3, y:y+3]
            if(len(sub_image_value) == 3 and len(sub_image_value[0]) == 3):
                new_image[x+1,y+1] = IEA[int("".join([str(_) for _ in sub_image_value.flatten()]),2)]

    input = new_image[1:-1,1:-1]

    if(_==1):
        part1 = np.count_nonzero(input[3:-3,3:-3])

for line in np.where(input[3:-3,3:-3],'█','░'):
    print("".join([_ for _ in line]))

print(f"Part1: {part1}")
print(f"Part2: {np.count_nonzero(input[3:-3,3:-3])}")