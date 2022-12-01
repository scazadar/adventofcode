#!/usr/bin/env python3
import json
input = [_ for _ in [x.strip() for x in open("demo.txt").readlines()]]

def get_outer_array(arr,cursor):
    arr_left = ""
    arr_right = ""
    sub_cursor = cursor - 2
    print(arr[sub_cursor])
    closingcount = 0
    while(arr[sub_cursor] != "[" or closingcount > 0):
        sub_cursor -= 1
        if(arr[sub_cursor] == "]"):
            closingcount += 1
        if(arr[sub_cursor] == "["):
            closingcount -= 1
        
        arr_left = arr[sub_cursor] + arr_left
        
    closingcount = 0
    while(arr[sub_cursor] != "]" or closingcount > 0):
        sub_cursor += 1
        if(arr[sub_cursor] == "["):
            closingcount += 1
        if(arr[sub_cursor] == "]"):
            closingcount -= 1
        arr_right = arr_right + arr[sub_cursor]
        

    
    print(json.loads(f"[{arr_left}{arr_right}]"))


def explode(arr):
    cursor = 0
    depth = 0

    for x in range(len(arr)):
        if(f"{arr[x]}" == "["):
            depth += 1
        elif(f"{arr[x]}" == "]"):
            depth -= 1
        cursor += 1

        exploding_pair = ""
        sub_cursor = cursor
        if(depth > 4):
            while(arr[sub_cursor] != "]"):
                exploding_pair += arr[sub_cursor]
                sub_cursor += 1
            exploding_pair = [int(_) for _ in exploding_pair.split(",")]
            arr = f"{arr[:cursor-1]}0{arr[sub_cursor+1:]}"
            print(arr[cursor-1])
            print(get_outer_array(arr,cursor))
            break

    return arr
    

def split(arr):
    #print("Split")
    arr_string = arr
    splitted = False
    for x in range(len(arr_string)):
        try:
            if(int(f"{arr_string[x]}{arr_string[x+1]}") > 9):
                arr_string = f"{arr_string[:x]}{[int(int(f'{arr_string[x]}{arr_string[x+1]}')/2),int(int(f'{arr_string[x]}{arr_string[x+1]}')/2+1)]}{arr_string[x+2:]}"
                splitted = True
                break
        except Exception:
            pass
    return arr_string, splitted

arr = "[[2,7],[[[[3,1],[3,2]],[4,3]],[[6,3],8]]]"

print(f"Start: {arr}")

arr = explode(arr)

#print("WRITE EXPLODED")
#print(exploded_left,exploded_right)

"""
if(exploded_right > 0):
    write_exploded_number_right(arr,exploded_right)
if(exploded_left > 0):
    write_exploded_number_left(arr,exploded_left)
if(exploded_left == -1 and exploded_right == -1):
    arr,splitted = split(arr)
print(arr)
if(exploded_left == -1 and exploded_right == -1 and not splitted):
    break
"""
    
    

print(f"Final {arr}")