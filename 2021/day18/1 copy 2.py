#!/usr/bin/env python3
import json
input = [_ for _ in [x.strip() for x in open("demo.txt").readlines()]]

def explode(arr):
    #print("Split")
    depth = 0
    cursor = 0
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
            
            if(arr[cursor] == ","):
                #arr = f"{arr[:cursor+1]}{int(arr[cursor+1])+exploding_pair[1]}{arr[cursor+2:]}"
                sub_cursor = cursor-3
                
                while(arr[sub_cursor] != ","):
                    sub_cursor -= 1
                if(arr[sub_cursor-1] == "["):
                    arr = f"{arr[:sub_cursor-1]}{int(arr[sub_cursor-1])+exploding_pair[0]}{arr[sub_cursor:]}"
                elif(arr[sub_cursor-1] == "]"):
                    arr = f"{arr[:sub_cursor-2]}{int(arr[sub_cursor-2])+exploding_pair[0]}{arr[sub_cursor-1:]}"

                sub_cursor = cursor
                while(arr[sub_cursor] != ","):
                    sub_cursor += 1
                if(arr[sub_cursor+1] == "["):
                    arr = f"{arr[:sub_cursor+2]}{int(arr[sub_cursor+2])+exploding_pair[1]}{arr[sub_cursor+3:]}"
                else:
                    arr = f"{arr[:sub_cursor+1]}{int(arr[sub_cursor+1])+exploding_pair[1]}{arr[sub_cursor+2:]}"
                
            elif(arr[cursor-2] == ","):
                arr = f"{arr[:cursor-3]}{int(arr[cursor-3])+exploding_pair[0]}{arr[cursor-2:]}"
                sub_cursor = cursor+2
                
                while(arr[sub_cursor] != ","):
                    if(sub_cursor >= len(arr)):
                        break
                    sub_cursor += 1
                print(arr)
                print(arr[sub_cursor])
                if(sub_cursor >= len(arr)):
                    if(arr[sub_cursor-1] == "["):
                        arr = f"{arr[:sub_cursor-1]}{int(arr[sub_cursor-1])+exploding_pair[0]}{arr[sub_cursor:]}"
                    elif(arr[sub_cursor-1] == "]"):
                        arr = f"{arr[:sub_cursor-2]}{int(arr[sub_cursor-2])+exploding_pair[0]}{arr[sub_cursor-1:]}"
                
                sub_cursor = cursor+2
                if(sub_cursor < len(arr)):
                    while(arr[sub_cursor] != ","):
                        sub_cursor -= 1
                    if(arr[sub_cursor-1] == "]"):
                        arr = f"{arr[:sub_cursor+2]}{int(arr[sub_cursor+2])+exploding_pair[1]}{arr[sub_cursor+3:]}"
                    else:
                        arr = f"{arr[:sub_cursor+1]}{int(arr[sub_cursor+1])+exploding_pair[1]}{arr[sub_cursor+2:]}"
            #print(arr[cursor-2])
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

arr = ["[[[[[9,8],1],2],3],4]","[7,[6,[5,[4,[3,2]]]]]","[[6,[5,[4,[3,2]]]],1]","[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]","[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"]

print(f"Start: {arr}")

for _ in arr:
    print(explode(_))
#arr = explode(arr)
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
    
    

#print(f"Final: {arr}")