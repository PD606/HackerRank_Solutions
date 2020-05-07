#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
l=[]

def pangrams(s):
    d=dict()
    s=s.lower()
    for w in s:
        if(w not in l and w!=' '):
            l.append(w)

    if(len(l)==26):
        return 'pangram'
    else:
        return 'not pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
