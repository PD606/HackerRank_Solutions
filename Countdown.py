#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    c=[]
    i=0
    while(i<len(arr)):
        ele=min(arr)
        for j in range(0,len(arr)):
            arr[j]-=ele

        c.append(len(arr))
        
        while(0 in arr):
            arr.remove(0)
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
T=int(input())
i=0
while i<T:
    i+=1
    cnt=0
    m,n=map(int,input().split(' '))
    l=list(map(int,input().split(' ')))
    l.append(0)
    # print(l)
    j=0
    p=1
    k=0

    if 1 not in l:
        k=0
       
        
    else:
        while(p<=m):
            # print('cccc',cnt)
            # print('pppp+',p)
            # print('gggggg',l[p-1])
            if((l[p-1]==1 and cnt==n-1) or (l[p-1]==l[p]+1) ):
                # print(l[p-1])
                cnt+=1
                # print('cnt',cnt)
                p+=1

                if(cnt==n):
                    # print('lll',cnt)
                     k+=1
                     cnt=0
            else:
                p+=1

    print('Case #{}:'.format(i),k)
    

    