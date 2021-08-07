n=int(input("Enter level"))
c=1
for i in range(0,n):
	for j in range(0,i):
		print(" ",end="")
	for j in range(0,n*2-c):
		print("*",end="")
	c+=2
	print()

	