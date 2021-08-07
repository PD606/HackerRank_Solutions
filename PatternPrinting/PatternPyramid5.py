n = int(input("Enter level"))

h=n//2+1

for i in range(0,h):
	for j in range(0,n-i):
		print(" ",end="")
	for j in range(0,i*2-1):
		print("*",end="")
	print()

for i in range(1,h):
	for j in range(0,i-1):
		print(" ",end="")
	for j in range(0,h*2-i):
		print("*",end="")
	print()