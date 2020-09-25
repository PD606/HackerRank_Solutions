def delchar(n,c):
	if(len(c) == 1):
		n=n.replace(c,'')
		return n
	else:
		return n
      
      
def shuffle(l1,l2):
	l3=[]
	c=0
	while( (c<len(l1)) and (c<len(l2))):
		l3.append(l1[c])
		l3.append(l2[c])
		c+=1

	if(len(l1)>c):
		l3.extend(l1[c:])

	if(len(l2)>c):
		l3.extend(l2[c:])

	return l3
  
  
def primeproduct(n):
	p=[]
	c=2
	
	while(c<=n):
		r=1
		i=2
		val=0
	
		while(i<c):
			if((c%i)==0):
				r=0
				break
			else:
				i+=1

		if(r==1):
			p.append(c)	
		c+=1
        
	for i in range(0,len(p)):
		for j in range(i+1,len(p)):
          
			res=p[i]*p[j]
         
			if(res==n):
				val=1
				break
       
                
	if(val==1):
		return True
	else:
		return False
					
          
          
          
