#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    jump_n = 0
    k_one = x1
    k_two = x2
    while(True):
        k_one = k_one + v1
        k_two = k_two + v2
        
        if k_one == k_two:
            return "YES"
        else:
            jump_n = jump_n + 1
            
        if v1 >= v2 and k_one > k_two:
            return "NO"
        elif v2 >= v1 and k_two > k_one:
            return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()