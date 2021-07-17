#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    sum_a = 0;
    sum_b = 0;
    for i in range(3):
        if a[i] > b[i]:
            sum_a = sum_a + 1
        elif b[i] > a[i]:
            sum_b = sum_b + 1
        else:
            continue
    
    return [sum_a, sum_b]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()