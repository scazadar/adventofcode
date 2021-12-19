#!/usr/bin/env python3
import json
input = [json.loads(_) for _ in [x.strip() for x in open("demo.txt").readlines()]]

def explode(arr):
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