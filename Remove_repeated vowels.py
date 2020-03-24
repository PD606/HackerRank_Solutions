l1=['a','e','i','o','u']
l2=[]
l3=[]
n=input()
l=len(n)
#print(l)

for i in range(l):
  if(n[i] in l1):
    j=i+1

    #print(j)
    if(j!=l and n[j] in l1):
      while(n[j] in l1):
        l3.append(n[i])
        n=n.replace(n[j],'_',1)    
    else:
      l3.append(n[i])
  else:
    l3.append(n[i])
l3="".join(l3)
print(l3.replace("_",""),end='')
