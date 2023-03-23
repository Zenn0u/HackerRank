#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    # for i in range(len(s)):
    #     for j in range(i+1,len(s)):
    #         print(f"{s[i]} + {s[j]} = {s[i]+s[j]}")

    mods = Counter(i % k for i in s)
    total = mods[0] > 0 # Because can only take single from here otherwise 0 + 0 == 0
    total += k%2 == 0 and mods[k//2] > 0 # Incase the array has odd numbered elements
    for i in range(1,  (k+1)//2):
        total += max(mods[i], mods[k-i])
    return total
                    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
