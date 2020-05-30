#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    c=0
    i=0
    s.append(0)
    while(i<len(s)):
        sum=0
        sm=s[i]
        j=i+1
        # if(k==len(s)):
        #     break
        try:
            while(j<m+i):
                sum=sum+s[j]
            # print(sum)
                j+=1

        except:
            pass

        i+=1
        ts=sum+sm

        # print(ts)

        if(ts==d):
            c+=1

  

    return (c)

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
