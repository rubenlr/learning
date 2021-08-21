#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    print(arr[0] + arr[1] + arr[2] + arr[3], end='')
    print(' ', end='')
    print(arr[1] + arr[2] + arr[3] + arr[4], end='')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
