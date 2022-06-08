#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    length = len(s)
    c_string = 0
    for i in range(length):
        if s[i] == 'a':
            c_string += 1
    tmp = int(n / length)
    count = tmp * c_string
    remain = n % length
    if remain != 0:
        for i in range(remain):
            if s[i] == 'a':
                count += 1
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()