#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    print(f"len: {len(s)} with range: {range(len(s) - m + 1)}")
    try:
        total = 0
        for i in range(len(s) - m + 1):
            if sum(s[i : i+m]) == d:
                total += 1
        return total
    except Exception:
        return 0
   
if __name__ == '__main__':
    print(birthday([4], 4, 1))
