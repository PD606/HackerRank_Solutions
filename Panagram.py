l1=[]
l2=[]
l3=[]
for x in range(97,123):
  l1.append(chr(x))

for x in range(65,91):
  l2.append(chr(x))

n=input()

n=n.upper()
#print(n)
c=0
for i in n:
  if(i in l3):
  	continue
  else:
    l3.append(i)
    # print(l3)
    if(i==' '):
      continue
    else:  
      c+=1
#print(c)    
if(c==26):
  print("YES")
else:
  print("NO")