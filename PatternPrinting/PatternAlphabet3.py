n = int(input("Enter level"))
a=65
for i in range(0,n):
	for j in range(0,n-i):
		print(chr(a),end="")
	a+=1
	print()