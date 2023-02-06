#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    max_n = 0
    n = 1
    for i in range(len(a)):
        n = 1
        for j in range(i+1, len(a)):
            if a[i] - a[j] == 0 or a[i] - a[j] == -1:
                n += 1

            if max_n <= n:
                max_n = n
    return max_n     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
