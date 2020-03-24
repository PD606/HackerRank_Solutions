s=input().split(" ")
l2=[]
n=set(s)

for i in s:
  if(i in n):
    if(i in l2):
      continue
    else:
      print(i,end=' ')
      l2.append(i)