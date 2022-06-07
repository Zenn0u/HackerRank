#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    
    arr_name = []
    arr_email = []
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        if emailID not in arr_email and "@gmail.com" in emailID:
            arr_name.append(firstName)
            arr_email.append(emailID)
        
    arr_name.sort()
    for i in arr_name:
        print(i)