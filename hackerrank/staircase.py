import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):    
    for row in range(0, n):
        for spaceCol in range(0, n - 1 - row):
            print(" ", end="")
        for sharpCol in range(0, row + 1):
            print("#", end="")
        print()

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
