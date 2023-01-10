#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    loc_a = abs(z - x)
    loc_b = abs(z - y)
    
    if loc_a == loc_b:
        return ("Mouse C")
    elif loc_a < loc_b:
        return ("Cat A")
    else:
        return ("Cat B")
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
