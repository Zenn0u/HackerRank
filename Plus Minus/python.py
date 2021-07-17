#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i  == 0:
            zero = zero + 1
        elif i > 0:
            pos = pos + 1
        else:
            neg = neg + 1
    print(str(pos/length))
    print(str(neg/length))
    print(str(zero/length))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)