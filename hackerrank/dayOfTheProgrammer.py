#!/bin/python3

import math
import os
import random
import re
import sys

def isLeap(year):
    if year > 1918 and year % 100 == 0 and year % 400 != 0:
        return False
    if year % 4 != 0:
        return False
    return True
    
def getMonthDays(m, y):
    if m == 2:
        if isLeap(y):
            print('leap')
            return 29
        else:
            print('no leap')
            return 28
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    return 30

def dayOfProgrammer(year):
    d, m, totalDays = 0, 0, 0
    
    for i in range(1, 12):
        currentMonthDays = getMonthDays(i, year)
        if (currentMonthDays + totalDays > 256):
            return f"{(256-totalDays):02}.{i:02}.{year:04}"
        
        totalDays += currentMonthDays

if __name__ == '__main__':
    print(dayOfProgrammer(1800))
