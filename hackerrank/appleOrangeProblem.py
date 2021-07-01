#!/bin/python3

import math
import os
import random
import re
import sys

def getFruidPosition(startPosition, position):
    return startPosition + position

def isInsideTheHouse(s, t, position):
    return position >= s and position <= t

def howFruidsAreInside(s, t, startPosition, fruits):
    insideTheHouseCounter = 0

    for fruit in fruits:
        position = getFruidPosition(startPosition, fruit)
        if isInsideTheHouse(s, t, position):
            insideTheHouseCounter += 1

    return insideTheHouseCounter

def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(howFruidsAreInside(s, t, a, apples))
    print(howFruidsAreInside(s, t, b, oranges))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
