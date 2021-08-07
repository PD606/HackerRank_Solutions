n=int(input("Enter level"))

for i in range(1,n+1):
	for j in range(0,n-i):
		print(" ",end="")
	for j in range(0,i*2-1):
		print("*",end="")
	print()

c=1
p=3
for i in range(1,n):
	for j in range(0,i):
		print(" ",end="")
	for j in range(0,n*2-p):
		print("*",end="")
	print()
	p+=2