N=int(input())

l=[1,N]
i=2

if(N==1):
	print(N)
	exit(0)
	
while(i<=N//2):
	if((N%i)==0):
		l.append(i)
	i+=1

l.sort()
j=0
while(j<len(l)):
	print(l[j],end=' ')
	j+=1