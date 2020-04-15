m,n=input().split(',')
m=int(m)
n=int(n)
f=0
even=['0','2','4','6','8']
l=[]
l2=[]


while(m<=n):
  if(m%2==0):
    l.append(m)
    m+=1
  else:
    m+=1
    continue
    
for i in l:
  i=str(i)
  for j in range(0,4):
    if(i[j] not in even):
      f=1
      break
    else:
      f=0
      continue
      
  if(f==0):
    l2.append(i)
  else:
    continue
l2=','.join(l2)
print(l2)