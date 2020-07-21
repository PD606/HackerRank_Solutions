n=int(input('number'))
arr=[]
i=0
c=0
while(i<n):
    ele=int(input())
    arr.append(ele)
    i+=1

s=int(input('search'))
o=int(input('occurence'))

for j in range(0,n):
    if(arr[j]==s):
        c+=1
        if(c==o):
            print(j)
    
            

