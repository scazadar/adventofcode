#!/usr/bin/env python3
# Imports
import time

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day19.sample"

towels,designs= open(file).read().split("\n\n")

towels = [_.strip() for _ in towels.split(",")]
designs = designs.split("\n")

print(towels)
print(designs)

   
        
        

# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))
