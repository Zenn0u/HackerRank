#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
# Had a timeout on 11th test
def freqQuery(queries):
    result = []
    freq = {}
    found = False
    
    for com, val in queries:
        cur = freq.get(val, 0)
        if com == 1:
            freq[val] = cur + 1
        elif com == 2:
            if cur != 0:
                freq[val] = cur - 1
        elif com == 3:
            for i in freq.values():
                if i == val:
                    found = True
                    result.append(1)
                    break
            if found == False:
                result.append(0)
            else:
                found = False
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
