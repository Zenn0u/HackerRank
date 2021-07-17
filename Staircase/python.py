#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        j = n - i - 1
        for l in range(j):
            print(" ", end="")
        for k in range(i+1):
            print("#", end="")
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)