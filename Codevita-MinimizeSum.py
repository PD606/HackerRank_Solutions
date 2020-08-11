import heapq
import math


m,n=input().split(' ')
# c=0
n=int(n)
arr=list(map(int,input().split(' ')))

arr=[20,7,5,4]
narr=[]
# print(arr)

for i in arr:
    narr.append(i*-1)

n=len(arr)-1

while(n):
    n-=1
    heapq.heapify(narr)
    ele=heapq.heappop(narr)
    # print(ele)
    heapq.heappush(narr,math.ceil(ele//2))
    # print(narr)

print(sum(narr)*-1)
