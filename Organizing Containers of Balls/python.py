#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    cont_type = list()
    size = len(container)
    for i in range(size):
        n = 0
        for j in range(size):
            n += container[j][i]
        cont_type.append(n)
    
    cont_sum = list()
    for i in range(size):
        n = 0
        for j in range(size):
            n += container[i][j]
        cont_sum.append(n)
        
    for i in range(size):
        if cont_type[i] not in cont_sum:
            return "Impossible"
            
    return "Possible"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
