#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    an_dict = {}
    count = 0
    
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            current = str(sorted(s[j:j+i]))
            
            if (current not in an_dict):
                an_dict[current] = 1
            else:
                count += an_dict[current]
                an_dict[current] += 1
                
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()