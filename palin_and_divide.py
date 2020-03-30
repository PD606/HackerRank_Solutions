two=[]
three=[]
four=[]
five=[]

class p():
	sum=0

def isPalin(n):
	d=n
	n=str(n)
	#print(type(a))
	n=reversed(n)
	
	n="".join(n)
	n=int(n)

	if(n==d):
		if(d%9==0):
			p.sum=p.sum+d
			#print(p.sum)
	#print(p.sum)

n=int(input("Enter n"))

if(n==3):
	for x in range(100,1000):
		three.append(x)
	for x in three:
		isPalin(x)

elif(n==4):
	for x in range(1000,10000):
		four.append(x)
	for x in four:
		isPalin(x)

elif(n==5):
	for x in range(10000,100000):
		five.append(x)
	for x in five:
		isPalin(x)

else:
	for x in range(10,100):
		two.append(x)
	for x in two:
		isPalin(x)
			
print(p.sum)