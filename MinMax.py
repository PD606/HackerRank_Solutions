#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    sum1=0
    sum2=0
    m1=max(arr)
    m2=min(arr)
    for i in range (0,len(arr)-1):
        sum1=sum1+arr[i]
    for i in range (1,len(arr)):
        sum2=sum2+arr[i]
    print(sum1,end=" ")
    print(sum2,end="")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
