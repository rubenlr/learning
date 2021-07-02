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

def diagonalDifference(arr):
    t = 0
    total = len(arr) - 1
    for i in range(0, len(arr)):
        t += arr[i][i] - arr[i][total - i]
    return abs(t)

if __name__ == '__main__':
    arr = [
[-10, 3, 0, 5, -4],
[2, -1, 0, 2, -8],
[9, -2, -5, 6, 0],
[9, -7, 4, 8, -2],
[3, 7, 8, -5, 0]

    ]
    res = diagonalDifference(arr)
    print("resultado: " + str(res))
