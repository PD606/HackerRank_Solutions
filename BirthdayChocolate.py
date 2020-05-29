#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    # print(s)
    i=0
    c=0

    if(len(s)==1):
        if(d == 1):
            return 1
    
    else:
        while(i<len(s)):
            sm=0
            for j in range(i+1,m+1):
                sm=sm+s[i]+s[j]
            # print(sm)
                if(sm == d):
                    c+=1
            i+=1

    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
