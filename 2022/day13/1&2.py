#!/usr/bin/env python3
#Imports
import time, json

#Zeit Start
start = time.time()

#Main
f = [[json.loads(_.strip()) for _ in _.split("\n")] for _ in open("inputs/day13.sample").read().split("\n\n")]

def convert(left,right):
    if(not isinstance(left, (list)) and isinstance(right, (list))):
        return [left],right
    elif(not isinstance(right, (list)) and isinstance(left, (list))):
        return left,[right]
    else:
        return left,right

def compare(left,right):
    left,right = convert(left,right)
    print(left,right)
    if(isinstance(left, (list)) and isinstance(right, (list))):
        for _ in range(len(left)):
            try:
                return compare(left[_],right[_])       
            except IndexError:
                return False

    elif(left < right):
        return True


  
indicies = []
x = 0



for pair in f:
    x += 1
    for _ in range(len(pair[0])):
        try:
            if(compare(pair[0][_],pair[1][_])):
                print(True)
                indicies.append(x)
                break
        except IndexError:
            pass
    else:
        print(True)
        #indicies.append(x)


print(indicies)


        


#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s