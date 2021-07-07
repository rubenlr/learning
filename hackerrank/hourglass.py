#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    res = 0
    for i in range(4):
        for j in range(4):
            hourglass = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            print(f"{i}:{j} = {hourglass}")
            res += hourglass
    return res

if __name__ == '__main__':
    print(hourglassSum([[-9, -9, -9, 1, 1, 1], 
                        [0, -9, 0, 4, 3, 2], 
                        [-9, -9, -9, 1, 2, 3], 
                        [0, 0, 8, 6, 6, 0], 
                        [0, 0, 0, -2, 0, 0], 
                        [0, 0, 1, 2, 4, 0]]))
