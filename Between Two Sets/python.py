#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def LCM(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm

def GCD(b):
    gcd = b[0]
    for i in b[1:]:
        gcd = math.gcd(gcd, i)
    return gcd

def getTotalX(a, b):
    # Write your code here
    lcm = LCM(a)
    gcd = GCD(b)
    
    count = 0
    multi = lcm
    while multi <= min(b):
        if gcd % (multi) == 0:
            count += 1
        multi += lcm
    
    return count
    




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()