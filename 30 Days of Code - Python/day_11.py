import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

max = None

for row in range(0,4):
    for col in range(0,4):
        top = arr[row][col] + arr[row][col+1] + arr[row][col+2]
        middle = arr[row+1][col+1]
        bottom = arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
        
        if max == None:
            max = top+middle+bottom
        elif max < top+middle+bottom:
            max = top + middle + bottom         
            
print(max)