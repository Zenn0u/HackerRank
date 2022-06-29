#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

# Test cases 1,2,3,4,5 fail because of timeouts
def activityNotifications(expenditure, d):
    # Write your code here
    notifications = 0
    for i in range(len(expenditure)-d):
        arr = expenditure[i:i+d]
        me = median(arr)
        expen = expenditure[i+d]
        if expen >= me*2:
            notifications += 1
    return notifications
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
