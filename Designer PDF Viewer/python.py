#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    al = "abcdefghijklmnopqrstuvwxyz"
    tallest = 0
    for i in word:
        for j in range(26):
            if i == al[j]:
                if tallest < h[j]:
                    tallest = h[j]
                    
    return tallest * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
