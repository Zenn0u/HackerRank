#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    game = 0
    min_s = 0
    min_n = 0
    max_s = 0
    max_n = 0
    for i in scores:
        if game == 0:
            min_s = i
            max_s = i
        elif min_s > i:
            min_s = i
            min_n = min_n + 1
        elif max_s < i:
            max_s = i
            max_n = max_n + 1
        game = game + 1

    return max_n, min_n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()