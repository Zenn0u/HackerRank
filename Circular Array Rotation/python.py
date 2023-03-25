#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    # tmp = list()
    # tmp_a = a
    # for i in range(k):
    #     for j in range(len(tmp_a)):
    #         if j == 0:
    #             tmp.append(tmp_a[-1])
    #         else:
    #             tmp.append(tmp_a[j-1])
    #     tmp_a = tmp
    #     tmp = list()
        
    # arr = list()
    # for i in queries:
    #     arr.append(tmp_a[i])
    # return arr
    
    k = k % len(a)
    tmp = a[-k:] + a[:-k]
    ret = list()
    for i in queries:
           ret.append(tmp[i])
    return ret
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
