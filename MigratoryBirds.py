#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    d=dict()

    for i in arr:
        if(i not in d):
            d[i]=1
        else:
            d[i]+=1

    k=list(d.keys())
    v=list(d.values())

    # print(k)
    # print(v)
    m=v.index(max(v))

    # print(m)

    return(k[m])



    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
