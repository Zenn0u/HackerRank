#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
# Incorrect way of implementation but my solution 5/13 fails
def countTriplets(arr, r):
    count = 0
    dict = {}
    for i in arr:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    
    for i in reversed(dict.keys()):
        x = dict[i]
        if i/r in dict: 
            y = dict[i/r]
        else:
            break
        if i/(r*r) in dict:
            z = dict[i/(r*r)]
        else:
            break
        count += x*y*z
        
    return count
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
