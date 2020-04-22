#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    # print(s)
    i=0
    c=0
    l=len(s)

    while(i<l):
        try:
            if(s[i]==s[i+1]):
                # print(s[i])
                # print(s[i+1])
                i+=1
                c+=1
                continue
            else:
                i+=1
                continue
        except:
            i+=1
            pass
    return c




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
