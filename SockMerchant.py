#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d=dict()
    i=0
    s=0
    while(i<n):
        if(ar[i] not in d):
            d[ar[i]]=1
        else:
            d[ar[i]]+=1
        i+=1


    print(d)

    v=list(d.values())

    print(v)

    j=0
    while(j<len(v)):
        if((v[j]//2)>0):
            s+=(v[j]//2)
        j+=1
    return s



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
