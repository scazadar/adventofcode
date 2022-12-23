#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main

f = [int(_.strip()) for _ in open("inputs/day20.sample").readlines()]


def print_output(temp_output):
    output = [0]*len(f)
    #print(temp_output)
    for _ in temp_output:
        output[temp_output[_][1]] = temp_output[_][0]
    return output

temp_output = {}

for _ in range(len(f)):
    temp_output.setdefault(_,[f[_],_])


for _ in range(len(f)):
    print("Before: ", print_output(temp_output))

    for x in range(temp_output[_][0]):
        if(temp_output[_][0] >= 0):
            new_index = temp_output[f[temp_output[_][1] + 1]][1]
            new_number = f[temp_output[_][1] + 1]
            
            temp_output[temp_output[_][1] + 1][1] = temp_output[_][1]
            f[temp_output[_][1] + 1] = f[temp_output[_][1]]
            temp_output[_][1] = new_index
            f[temp_output[_][1]] = new_number





    """
    old_index = temp_output[_][1]
    new_index = temp_output[_][0] + temp_output[_][1]
    #print(new_index)
    while(new_index > len(f) -1):
        new_index -= len(f)
    while(new_index < 0):
        new_index += len(f)
    print(new_index)
    temp_output[_][1] = new_index

    for number in temp_output:
        new_temp_index = 0
        if(new_index > old_index):
        if(temp_output[_][0] >= 0 and temp_output[number][1] <= new_index and not number == _):
            new_temp_index = temp_output[number][1] - 1
            while(new_temp_index < 0):
                new_temp_index += len(f) 
            temp_output[number][1] = new_temp_index
        if(temp_output[_][0] < 0 and temp_output[number][1] >= new_index and not number == _):
            new_temp_index = temp_output[number][1] + 1
            while(new_temp_index > len(f) -1):
                new_temp_index -= len(f) 
            temp_output[number][1] = new_temp_index
    """

    print("After:  ", print_output(temp_output))





#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s