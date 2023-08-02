#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
        shift = arr[n-1]
        j = n-1
        for i in range(n-1, 0, -1):
            if shift < arr[j-1] and j >= 1:
                arr[j] = arr[j-1]
                j = j-1
                print(*arr)
            else:
                arr[j] = shift
                print(*arr)
                break
        else:
            arr[0] = shift
            print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
