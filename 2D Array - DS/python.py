#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    high_num = -1000
    row = len(arr)
    col = len(arr[0])
    
    for i in range(row-2):
        for j in range(col-2):
            cur_num = 0
            cur_num += arr[i][j]
            cur_num += arr[i][j+1]
            cur_num += arr[i][j+2]
            
            cur_num += arr[i+1][j+1]
            
            cur_num += arr[i+2][j]
            cur_num += arr[i+2][j+1]
            cur_num += arr[i+2][j+2]
 
            if cur_num > high_num:
                high_num = cur_num
            
    return high_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()