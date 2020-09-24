n=input('Enter String\n')

i=0
c=1
j=len(n)-1

while (i<j):
	if(n[i]==n[j]):
		i+=1
		j-=1
	else:
		c=0
		break
	
if(c==0):
	print('Not Palindrome')
else:
	print('Palindrome')
