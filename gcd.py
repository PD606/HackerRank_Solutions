def gcd(a,b):
	if(b==0):
		return a
	else:
		return gcd(b,a%b)


def isco(arr,n):
	c=0
	for i in range(0,n):
		for j in range(1,n-1):
			v=gcd(arr[i],arr[j])
			if(v==1):
				c+=1
			else:
				pass
	return c

# a=gcd(11,20)
# print(a)

n=int(input('size'))
i=0
arr=[]
while(i<n):
	i+=1
	a=int(input())
	arr.append(a)

print(arr)

res=isco(arr,n)

print('coprimes',res)

