#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    bin_n = bin(n)[2:]
    max_len = len(max(bin_n.split('0')))
    print(max_len)