#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos, neg, zero = 0.0, 0.0, 0.0

    for n in arr:
        if (n > 0):
            pos += 1
        elif (n < 0):
            neg += 1
        else:
            zero += 1

    s = len(arr)
    
    print("%.5f" % (pos / s))
    print("%.5f" % (neg / s))
    print("%.5f" % (zero / s))

if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
