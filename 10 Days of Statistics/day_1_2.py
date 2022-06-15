#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = []
    n = len(values)
    for i in range(n):
        for j in range(freqs[i]):
            arr.append(values[i])
        
    arr.sort()
    n = len(arr)
    mid = n//2
    
    Q1 = float(median(arr[:mid]))
    Q3 = float(median(arr[-mid:]))
    
    print(Q3-Q1)

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
