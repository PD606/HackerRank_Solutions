# arr=[-2,5,3,-1]
# arr=[-3,-2,5,-1]
arr=[1,-3,2,-5,7,6,-1,-4,11,-23]

s=-9999
ans=-9999

for i in range(0,len(arr)):
    if((arr[i]+s) > 0):
        s=arr[i]+s
        ans=max(s,ans)
    else:
        s=0

if(ans == -9999):
    ans=max(arr)

print(ans)
