#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count  = 0
    arr_dic = {j: i for i,j in enumerate(arr)}
    for i in range(len(arr)):
        if arr[i] != i+1:
            #index = arr.index(i+1,i)
            index = arr_dic[i+1]
            arr_dic[i+1], arr_dic[arr[i]] = i, index
            arr[i], arr[index] = arr[index], arr[i]
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()