# Title: Intro to Conditional Statements 

#!/bin/python3

import math
import os
import random
import re
import sys

def cond(N):
    if (N % 2 == 1):
        print("Weird")
    elif (N >= 2) and (N <= 5):
        print("Not Weird")
    elif (N >= 6) and (N <= 20):
        print("Weird")
    elif (N > 20):
        print("Not Weird")

if __name__ == '__main__':
    N = int(input().strip())
    cond(N)