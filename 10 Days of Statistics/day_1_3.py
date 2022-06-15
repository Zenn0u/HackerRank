#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import mean
from math import sqrt

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    arr_mean = mean(arr)
    total = 0
    for i in arr:
        total += ((i-arr_mean)**2)
    
    tmp = total/len(arr)
    print("%.1f"%tmp**(0.5))
    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
