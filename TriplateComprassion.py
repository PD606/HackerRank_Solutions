#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ca=0
    cb=0
    for i in range (0,3):
        if (a[i]>b[i]):
            ca=ca+1
        elif(a[i]==b[i]):
            continue
        else:
            cb=cb+1 
    return ca,cb
  
    
if (__name__=='__main__') :
        
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
