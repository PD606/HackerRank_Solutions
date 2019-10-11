#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    if ('PM' in s):
       t=s.split(":")
       hh=t[0]
       mm=t[1]
       ss=t[2]
       print(t[1])
      #print(hh[0])
      # hh=int(hh[0])+12
       mm=int(s[3])
       print (mm)
     

if ( __name__ == '__main__' ):

    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
