n=int(input("Enter level"))

for i in range(0,n):
	for j in range(1,n-i):
		print(" ",end="")
	for j in range(0,i+1):
		print("* ",end="")
	print()
