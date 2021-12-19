#!/usr/bin/env python3
import json
input = [json.loads(_) for _ in [x.strip() for x in open("demo.txt").readlines()]]

def explode(arr,depth=0):
    depth += 1
    exploded_left = -1
    exploded_right = -1
    if(type(arr[0]) == list):
        exploded_left,exploded_right,exploded = explode(arr[0],depth)
        if(exploded):
            
            arr[0] = 0
            arr[1] += exploded_right
            exploded_right = 0
            return exploded_left,exploded_right,False

    elif(type(arr[1]) == list and exploded_right == -1):
        exploded_left,exploded_right,exploded = explode(arr[1],depth)
        if(exploded):
            arr[1] = 0
            arr[0] += exploded_left
            exploded_left = 0
            return exploded_left,exploded_right,False
    elif(depth > 4):
        return arr[0],arr[1],True
    return exploded_left,exploded_right,False

def write_exploded_number_left(arr,left,first=True):
    done = False
    if(first):
        try:
            if(type(arr[0]) == int and not done):
                arr[0] += left
                return True
            if(type(arr[0]) == list):
                done = write_exploded_number_left(arr[0],left,False)
        except TypeError:
            return False
    else:
        try:
            if(type(arr[1]) == int and not done):
                arr[1] += left
                return True
            if(type(arr[1]) == list):
                done = write_exploded_number_left(arr[1],left,False)
        except TypeError:
            return False

def write_exploded_number_right(arr,right,first=True):
    done = False
    if(first):
        try:
            if(type(arr[1]) == int and not done):
                arr[1] += right
                return True
            if(type(arr[1]) == list):
                done = write_exploded_number_right(arr[1],right,False)
        except TypeError:
            return False
    else:
        try:
            if(type(arr[0]) == int and not done):
                arr[0] += right
                return True
            if(type(arr[0]) == list):
                done = write_exploded_number_right(arr[0],right,False)

        except TypeError:
            return False

def split(arr):
    #print("Split")
    arr_string = str(arr)
    splitted = False
    for x in range(len(arr_string)):
        try:
            if(int(f"{arr_string[x]}{arr_string[x+1]}") > 9):
                arr_string = f"{arr_string[:x]}{[int(int(f'{arr_string[x]}{arr_string[x+1]}')/2),int(int(f'{arr_string[x]}{arr_string[x+1]}')/2+1)]}{arr_string[x+2:]}"
                splitted = True
                break
        except Exception:
            pass
    return json.loads(arr_string), splitted



    

arr = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]

while(True):
    exploded_left,exploded_right,exploded = explode(arr)
    #print("WRITE EXPLODED")
    #print(exploded_left,exploded_right)
    if(exploded_right > 0):
        write_exploded_number_right(arr,exploded_right)
    if(exploded_left > 0):
        write_exploded_number_left(arr,exploded_left)
    if(exploded_left == -1 and exploded_right == -1):
        arr,splitted = split(arr)
    print(arr)
    if(exploded_left == -1 and exploded_right == -1 and not splitted):
        break
    
    

print(arr)