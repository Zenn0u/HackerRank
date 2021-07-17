#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    conv = ""
    if s[8] + s[9] == "AM":
        tmp = s[0] + s[1]
        if tmp == "12":
            tmp = "00"
        conv = conv + tmp
        for i in range(2,8):
            conv = conv + s[i]
    else:
        tmp = str(int(s[0] + s[1]) + 12)
        if tmp == "24":
            tmp = "12"
        conv = conv + str(tmp)
        for i in range(2,8):
            conv = conv + s[i]
            
    return conv
        
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()