# arr = list(map(int,(input().split(' '))))


# arr = list(map(int,input().split(' ')))
# print(arr)
arr = input().split(' ')
print(arr)

d=dict()

for i in arr:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1

s=0

val = list(d.values())
key= list(d.keys())

print(val)
print(key)

for j in val:
    if((j % 2)==1):
        s+=int(key[val.index(j)])*j
        
    
print(s-1)



