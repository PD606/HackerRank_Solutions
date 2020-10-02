def contracting(n):
	i=0
	j=1
	p=1
	tmp=999
	while(i<len(n)-1):
		diff=abs(n[i]-n[j])
		print(diff)
		if(tmp<=diff):
			p=0
			break
		else:
			tmp=diff
			i+=1
			j+=1

	if(p==1):
		return True
	else:
		return False

# g=contracting([9,2,7,3,1])
# g=contracting([-2,3,7,2,-1])

# g=contracting([10,7,4,1])
# print(g)


def leftrotate(n):
	i=len(n)-1
	fl=[]
	while(i>=0):
		tl=[]
		for j in range(0,len(n)):
			tl.append(n[j][i])
		fl.append(tl)
		i-=1
	return fl

# leftrotate([[1,2],[3,4]])
# leftrotate([[1,2,3],[4,5,6],[7,8,9]])

def counthv(n):
	i=1
	j=0
	k=i+1
	h=0
	v=0

	while(k<len(n)):
		if(n[i]>n[j] and n[i]>n[k]):
			h+=1
			i+=1
			j+=1
			k+=1
		elif(n[i]<n[j] and n[i]<n[k]):
			v+=1
			i+=1
			j+=1
			k+=1
		else:
			i+=1
			j+=1
			k+=1

	# print(h)
	# print(v)
	return [h,v]

# counthv([1,2,1,2,3,2,1])
# p=counthv([1,2,3,1])
# print(p)

