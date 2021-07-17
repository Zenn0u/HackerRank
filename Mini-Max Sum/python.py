#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_n = 0
    max_n = 0
    smallest = min(arr)
    largest = max(arr)
    
    if smallest == largest:
        for i in arr:
            max_n = max_n + i
        max_n = max_n - largest
        print(str(max_n) + " " + str(max_n))
    else:
        for i in arr:
            if i == smallest:
                min_n = min_n + i
            elif i == largest:
                max_n = max_n + i
            else:
                max_n = max_n + i
                min_n = min_n + i
        
        print(str(min_n)+ " " + str(max_n))
        
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)