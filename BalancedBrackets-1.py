#!/bin/python3

import math
import os
import random
import re
import sys

#Complete the isBalanced function below.

def isBalanced(s):
    c=1
    l=[]

    for i in s:

        if((i=='(') or (i=='{') or (i=='[')):
            l.append(i)

        else:

            if(len(l)<=0):
                print("LOLOOO")
                c=0
                break

            ele=l.pop()

            if ( ( (ele=='(') and (i==')') ) or 
            ( (ele=='[') and (i==']') ) or 
            ( (ele=='{') and (i=='}') ) ):
                continue
            else:
                c=0
                break

    print(l)

    if(c==1):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
