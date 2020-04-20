#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    s=list(s)
    st=0
    l1=[]
    l2=['{','(','[']
    i=0
    while(i<len(s)):
        print('dddddd',s[i])

        if(s[i] in l2):
            print(s[i])
            l1.append(s[i])
            i+=1

        else:
            print(l1)
            le=len(l1)
            if(le != 0):
                ele=l1.pop(le-1)
                print('eeeeeeeeeeee',ele)
                print('ssssssss',s[i])
                if((ele=='(' and s[i]==')') or 
                (ele=='{' and s[i]=='}') or 
                (ele=='[' and s[i]==']') ):
                    print('plfkepfkp')
                    i+=1
                    continue 
                else:
                    st=1
                    break
            else:
                st=1
                break

    if(st==0):
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
