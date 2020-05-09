#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
d=[]
r=[]
def beautifulDays(i, j, k):
    c=0
    for m in range(i,j+1):
        d.append(m)
    # print(d)

    for n in d:
        # n=list(n)
        # print(n)
        n=str(n)
        # print(list(n))
        r.append(n[::-1])
    # print((r))

    for p in range(0,len(d)):
        z=((float(d[p])-float(r[p]))/k)
        # print(z)
        if(z.is_integer() or z==0):
            c+=1
        else:
            pass
    return (c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
