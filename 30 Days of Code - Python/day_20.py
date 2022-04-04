#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    totalSwaps = 0
    for i in range(0,n):
        numberOfSwaps = 0
        for j in range (0, n-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numberOfSwaps += 1
        if numberOfSwaps == 0:
            break
        totalSwaps += numberOfSwaps
    
    print(f"Array is sorted in {totalSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")