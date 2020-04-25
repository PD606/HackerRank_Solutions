#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
x=0
y=0
def pairs(k, arr):
    c=0
    for i in range(0,len(arr)):
        print('ppp')
        for j in range(0,len(arr)):
            x=arr[i]
            y=arr[j]
            if(x>y and (x-y)==k):
                c+=1
            else:
                continue
    return c



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
