#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    c=[]
    i=0
    while(i<len(arr)):
        ele=min(arr)
        for j in range(0,len(arr)):
            arr[j]-=ele

        c.append(len(arr))
        
        while(0 in arr):
            arr.remove(0)
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
