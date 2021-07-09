#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    distinctArr = set(arr)
    
    maxNum = 0
    maxNumCounter = 0
    
    for distinctNum in distinctArr:
        counter = arr.count(distinctNum)
        if counter > maxNumCounter:
            maxNum = distinctNum
            maxNumCounter = counter
        
    return maxNum   

if __name__ == '__main__':
    print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))