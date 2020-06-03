#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    d=dict()
    i=0
    while(i<len(arr)):
        if(arr[i] not in d):
            d[arr[i]]=1
        else:
            d[arr[i]]+=1
        i+=1

    k=list(d.keys())
    v=list(d.values())

    print(d)
    # m=v.index(max(v))
    # print(k[m])
    m=(max(v))
    
    p=len(arr)-m
    return p


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
