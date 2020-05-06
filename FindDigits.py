#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    s=n
    c=0
    while(n>0):
        rem=n%10
        n=n//10
        # print(s)
        try:
            if(s%rem==0):
                c+=1
            else:
                pass
        except:
            pass

    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
