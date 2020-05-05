#code

T=int(input())
i=0

while(i<T):
   d=dict()
   i+=1
   m=int(input())
   n=input().split(' ')
   for j in n:
    if(j not in d):
        d[j]=1
    else:
        d[j]+=1
        
   k=list(d.keys())
   v=list(d.values())
   ind=v.index(max(v))
#   print(ind)
#   print(k)
#   print(v)
#   print(ind)
#   print(k[ind])
#   print(k[ind])
   if(max(v)==1):
       print(n[len(n)-1])
   else:
       print(k[ind])

    