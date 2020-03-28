l1=[]
l2=[]
l3=[]


for i in range(65,91):
  l1.append(chr(i))
  
for i in range(97,123):
  l2.append(chr(i)) 

n=input()

for i in n:
  
  if(i in l1):
    i=ord(i)
    l3.append(chr(i+32))
  elif(i in l2):
    i=ord(i)
    l3.append(chr(i-32))
  else:
    l3.append(i)
    
l3="".join(l3)
print(l3)